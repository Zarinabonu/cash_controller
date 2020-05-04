import datetime
from operator import gt, lt, ge, le

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView

from app.model import Spravichnik, Main, Saldo, Department


class DepartmentListView(LoginRequiredMixin, TemplateView):
    template_name = 'department/list.html'

    def get_context_data(self, **kwargs):
        user = Department.objects.all()
        context = {
            'dept': user

        }
        return context


class DepartmentCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'department/create.html'


class DepartmentUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'department/update.html'
    pk_url_kwarg = 'id'
    queryset = Department.objects.all()
    context_object_name = 'department'


class SpravichnikListView(LoginRequiredMixin, TemplateView):
    template_name = 'spravichnik/list.html'

    def get_context_data(self, **kwargs):
        sp = Spravichnik.objects.all()
        context = {
            'sprav': sp

        }
        return  context


class SpravichnikUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'spravichnik/update.html'
    pk_url_kwarg = 'id'
    queryset = Spravichnik.objects.all()
    context_object_name = 'spravchnik'

    def get_context_data(self, **kwargs):
        context = super(SpravichnikUpdateView, self).get_context_data(**kwargs)
        # context['dep'] = Department.objects.all()
        return context


class SpravichnikCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'spravichnik/create.html'

    def get_context_data(self, **kwargs):
        # det = Department.objects.all()
        context = {
            # 'depts': det

        }
        return context

class MainListView(LoginRequiredMixin, TemplateView):
    template_name = 'main/list.html'

    def get_context_data(self, **kwargs):
        # context = super(MainListView, self).get_context_data(**kwargs)
        provodka = self.request.GET.get('provodka')
        date_search2 = self.request.GET.get("date_search")
        print('date issss', date_search2)

        m = Main.objects.all()
        sal = Saldo.objects.all()

        request = self.request.user.id
        user_request = User.objects.get(id=request)
        m = m.filter(Q(rasxod__department__user=user_request) | Q(prixod__department__user=user_request) )
        ma = m.filter(date_main__year=datetime.datetime.today().year).filter(date_main__month=datetime.datetime.today().month)
        sald = sal.filter(date_saldo__year=datetime.datetime.today().year).filter(spravichnik__department__user=user_request).filter(date_saldo__month=datetime.datetime.today().month)
        context = {
            'main': ma,
            'saldo': sald
        }
        if date_search2:
            userinput = str(date_search2)
            due = datetime.datetime.strptime(userinput, '%Y-%m-%d').date()
            print('sana ', due.year, 'month', due.month)
            sal = sal.filter(spravichnik__department__user=user_request).filter(date_saldo__year=due.year).filter(date_saldo__month=due.month)
            m = m.filter(date_main__year=due.year).filter(date_main__month=due.month)
            print('saldo', sal)
            context = {
                'main': m,
                'date_search': date_search2,
                'saldo': sal

            }

        return context


class IncomeListView(LoginRequiredMixin, TemplateView):
    template_name = 'income/list.html'

    def get_context_data(self, **kwargs):
        m = Main.objects.all()
        request = self.request.user.id
        user_request = User.objects.get(id=request)
        spravichnik = Spravichnik.objects.get(department__user=user_request)
        print(';REQUEST USER', spravichnik.id)
        m = m.filter(prixod=spravichnik)
        context = {
            'rasxod': m
        }
        return context


class IncomeUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'income/update.html'
    context_object_name = 'prixod'
    pk_url_kwarg = 'id'
    queryset = Main.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IncomeUpdateView, self).get_context_data(**kwargs)
        context['spr'] = Spravichnik.objects.all()
        return context


class IncomeCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'income/create.html'

    def get_context_data(self, **kwargs):
        date_search2= self.request.GET.get('date_search')
        request = self.request.user.id
        user_request = User.objects.get(id=request)
        datee = datetime.datetime.today().date()
        # strftime('%d-%m-%Y')
        m = Main.objects.all()
        sal = Saldo.objects.all()

        m = m.filter(prixod__department__user=user_request)
        ma = m.filter(date_main__year=datetime.datetime.today().year).filter(date_main__month=datetime.datetime.today().month)
        sald = sal.filter(date_saldo__year=datetime.datetime.today().year).filter(date_saldo__month=datetime.datetime.today().month)
        sp = Spravichnik.objects.all()
        context = {
            'prixod': ma,
            'spr': sp,
            'date': datee,
            'saldo': sald

        }
        if date_search2:
            userinput = str(date_search2)
            due = datetime.datetime.strptime(userinput, '%Y-%m-%d').date()
            print('sana ', due.year, 'month', due.month)
            sal = sal.filter(spravichnik__department__user=user_request).filter(date_saldo__year=due.year).filter(
                date_saldo__month=due.month)
            m = m.filter(date_main__year=due.year).filter(date_main__month=due.month)
            print('saldo', sal)
            context = {
                'prixod': m,
                'date_search': date_search2,
                'saldo': sal,
                'spr': sp,
                'date': datee,



            }

        return context



class MainUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'main/update.html'
    context_object_name = 'rasxod'
    pk_url_kwarg = 'id'
    queryset = Main.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MainUpdateView, self).get_context_data(**kwargs)
        context['spr'] = Spravichnik.objects.all()
        return context


class PrixodCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'main/prixod.html'

    def get_context_data(self, **kwargs):
        pri = Main.objects.all()
        useer = Department.objects.all()
        context = {
            'prixod': pri,
            'user': useer
        }
        return context


class RasxodCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'rasxod/rasxod.html'

    def get_context_data(self, **kwargs):
        request = self.request.user.id
        date_search2 = self.request.GET.get('date_search')
        user_request = User.objects.get(id=request)
        datee = datetime.datetime.today().date()


        rasxod = Main.objects.all()
        sal = Saldo.objects.all()

        rasxod = rasxod.filter(rasxod__department__user=user_request)
        ras = rasxod.filter(date_main__year=datetime.datetime.today().year).filter(date_main__month=datetime.datetime.today().month)
        sald = sal.filter(date_saldo__year=datetime.datetime.today().year).filter(date_saldo__month=datetime.datetime.today().month)
        useer = Spravichnik.objects.all()
        context = {
            'rasxod': ras,
            'user': useer,
            'date': datee,
            'saldo': sald
        }
        if date_search2:
            userinput = str(date_search2)
            due = datetime.datetime.strptime(userinput, '%Y-%m-%d').date()
            print('sana ', due.year, 'month', due.month)
            sal = sal.filter(spravichnik__department__user=user_request).filter(date_saldo__year=due.year).filter(
                date_saldo__month=due.month)
            m = rasxod.filter(date_main__year=due.year).filter(date_main__month=due.month)
            print('saldo', sal)
            context = {
                'rasxod': m,
                'date_search': date_search2,
                'saldo': sal,
                'user': useer,
                'date': datee,

            }

        return context


class RasxodUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'rasxod/update.html'
    pk_url_kwarg = 'id'
    queryset = Main.objects.all()
    context_object_name = 'rasxod'

    def get_context_data(self, **kwargs):
        context = super(RasxodUpdateView, self).get_context_data(**kwargs)
        context['spravichnik'] = Spravichnik.objects.all()
        return context


class SaldoCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'saldo/create.html'

    def get_context_data(self, **kwargs):
        sp = Spravichnik.objects.all()
        context = {
            'spr':sp
        }
        return context


class SaldoListView(LoginRequiredMixin, TemplateView):
    template_name = 'saldo/list.html'

    def get_context_data(self, **kwargs):
        s = Saldo.objects.all()
        request = self.request.user.id
        user_request = User.objects.get(id=request)
        spravichnik_request = Spravichnik.objects.get(user=user_request)
        s = s.filter(spravichnik=spravichnik_request)
        spra = Spravichnik.objects.all()
        spravichnik_search = self.request.GET.get('spravichnik_search')
        start_search = self.request.GET.get('start_search')
        finish_search = self.request.GET.get('finish_search')
        print('START ', start_search)
        print('FINISH', finish_search)

        if spravichnik_search:
            s = s.filter(spravichnik=spravichnik_search)
        if start_search:
            s = s.filter(date_saldo__gte=start_search)
            # print('DATE ', s.date_saldo)
        if finish_search:
            s = s.filter(date_saldo__lte=finish_search)
            # print('DATE2 ', s.date_saldo)

        context = {
            'sal': s,
            'spr': spra,

        }
        return context


# class LoginView(TemplateView):
#     template_name = 'login.html'
#
#     def get_context_data(self, **kwargs):
#         sp = Spravichnik.objects.all()
#         context = {
#             'spr': sp
#         }
#         return context


# class Login(View):
#     print('shag 1')
#
#     def get(self, request):
#         return render(request, 'login.html')
#         print('shag 2')
#
#     def get_context_data(self, **kwargs):
#         sp = Spravichnik.objects.all()
#         context = {
#             'spr': sp
#         }
#         return context
#
#     def post(self, request):
#         username = request.POST['user']
#         password = request.POST['password']
#         print('user', username)
#         print('user', password)
#
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#
#         return redirect(reverse('rasxod-list'))

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
        print('shag 2')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        print('user', username)
        print('user', password)
        user = authenticate(request, username=username, password=password)
        # user = User.objects.get(username=username, password=password)
        if user:
            login(request, user)

            # return render(request, 'main/list.html', {'date_search2': date_search})
            return HttpResponseRedirect(reverse('rasxod-list'))
        return render(request, 'login.html', {'error': True})

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

#     https://flask-login.readthedocs.io/en/latest/


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))


class StatisticaView(TemplateView):
    template_name = 'dashboard.html'






