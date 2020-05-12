import datetime
from decimal import Decimal
from fileinput import filename
from operator import gt, lt, ge, le

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView

from app.excel_tool import excel_2
from app.model import Spravichnik, Main, Saldo, Department
from itertools import chain



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
        main_list = []
        prixod_list = []
        rasxod_list = []
        list = []
        p_l = []
        r_l = []
        rasxod_sum = 0
        prixod_sum = 0
        today_date = datetime.datetime.today().date()
        request_user = self.request.user
        user = User.objects.get(id=request_user.id)
        department = Department.objects.get(user=user)
        main = Main.objects.all()
        saldo = Saldo.objects.all()

        main = main.filter(date__year=datetime.datetime.today().year).filter(date__month=datetime.datetime.today().month)
        main = main.filter(Q(rasxod__department__user=user)| Q(prixod__department__user=user))
        for mains_lists in main:
            rasxod = main.filter(id=mains_lists.id).filter(rasxod__department__user=user).values_list('summa', flat=True).first()
            prixod = main.filter(id=mains_lists.id).filter(prixod__department__user=user).values_list('summa', flat=True).first()

            prixod_list.append(prixod)
            main_list.append(mains_lists)
            rasxod_list.append(rasxod)
            pri = main.filter(id=mains_lists.id).filter(prixod__department__user=user)
            # for p in pri:
            #     p_l.append(p)
            #     print('prixod 22', p_l)
            #
            # ras = main.filter(id=mains_lists.id).filter(rasxod__department__user=user).first()
            # for r in ras:
            #     r_l.append(r)
            #     print('rasxod 22', r_l)

        print('main', main_list)
        print('prixod', prixod_list)
        print('rasxod', rasxod_list)
        print('prixod44', p_l)
        print('rasxod44', r_l)
        list.append(main_list)
        list.append(p_l)
        list.append(r_l)
        print('list', list)

        response = [{'main': m, 'prixod': p, 'rasxod': r} for m, p, r in zip(main_list, prixod_list, rasxod_list)]

        saldo_month_ago = saldo.filter(date_saldo__year=datetime.datetime.today().year).filter(
            date_saldo__month=datetime.datetime.today().month - 1).filter(spravichnik__department__user=user)
        for sal in saldo_month_ago:
            sal_month_ago = Decimal(sal.count_saldo)
            sal_month_ago = float(sal_month_ago)


        context = {
            'main':response,
            # 'month_ago_saldo': saldo_month_ago,
            # 'rasxod_sum': rasxod_sum,
            # 'prixod_sum': prixod_sum,
            # # 'saldo_now': sal_month_ago+prixod_sum-rasxod_sum,
            # 'today': today_date,

        }
        #
        # prixod_list = []
        # rasxod_list = []
        # main_id_lis = []
        #
        # # context = super(MainListView, self).get_context_data(**kwargs)
        # provodka = self.request.GET.get('provodka')
        # date_search2 = self.request.GET.get("date_search")
        # print('date issss', date_search2)
        #
        # main_base = Main.objects.all()
        #
        # request = self.request.user.id
        # user_request = User.objects.get(id=request)
        # main_b = main_base.filter(date_main__year=datetime.datetime.today().year).filter(date_main__month=datetime.datetime.today().month)
        # sald = sal.filter(date_saldo__year=datetime.datetime.today().year).filter(spravichnik__department__user=user_request).filter(date_saldo__month=datetime.datetime.today().month)
        #
        # for main in main_b:
        #     m = main_base.filter(Q(rasxod__department__user=user_request) | Q(prixod__department__user=user_request)).filter(id=main.id)
        #     print('main is', m)
        #     # rasxod = main_base.filter(id=main.id)
        #     # prixod = main_base.filter(prixod__department__user=user_request)
        #     main_id_lis.append(m)
        #     # rasxod_list.append(rasxod)
        #     # prixod_list.append(prixod)
        # print('main_list', main_id_lis)
        # rasxod = main_base.filter(rasxod__department__user=user_request)
        # for ras in rasxod:
        #     rasxod_list.append(ras)
        # print('rasxod_list', rasxod_list)
        # prixod = main_base.filter(prixod__department__user=user_request)
        # for pri in prixod:
        #     prixod_list.append(pri)
        # print('prixod_list', prixod_list)
        #
        # for rasxodlar in rasxod:
        #     rasxod_sum += rasxodlar.summa
        # for prixodlar in prixod:
        #     prixod_sum += prixodlar.summa
        # response = [{'main': main_id_lis, 'prixod': prixod_list, 'rasxod': rasxod_list} for main_id_lis, prixod_list, rasxod_list in zip(main_id_lis, prixod_list, rasxod_list)]
        # print('response', response)
        # context = {
        #     'main': response,
        #     'saldo': sald,
        #     'month_ago_saldo': saldo,
        #
        # }
        # if date_search2:
        #     userinput = str(date_search2)
        #     due = datetime.datetime.strptime(userinput, '%Y-%m-%d').date()
        #     print('sana ', due.year, 'month', due.month)
        #     sal = sal.filter(spravichnik__department__user=user_request).filter(date_saldo__year=due.year).filter(date_saldo__month=due.month)
        #     saldoo = sal.filter(date_saldo__year=due.year).filter(
        #         date_saldo__month=due.month - 1).filter(
        #         spravichnik__department__user=user_request)
        #     m = m.filter(date_main__year=due.year).filter(date_main__month=due.month)
        #     print('saldo', sal)
        #     context = {
        #         'main': m,
        #         'date_search': date_search2,
        #         'saldo': sal,
        #         'month_ago_saldo': saldoo
        #
        #
        #     }

        return context


class ExcelView(View):
    def get(self, request):
        filename = 'cash_control.xlsx'
        main_list = []
        prixod_list = []
        rasxod_list = []
        rasxod_sum = 0
        prixod_sum = 0
        today_date = datetime.datetime.today().date()

        request_user = self.request.user
        user = User.objects.get(id=request_user.id)
        department = Department.objects.get(user=user)
        main = Main.objects.all()
        saldo = Saldo.objects.all()

        main = main.filter(date_main__year=datetime.datetime.today().year).filter(
            date_main__month=datetime.date.today().month).filter(
            Q(rasxod__department__user=user) | Q(prixod__department__user=user))

        for main_lists in main:
            main_list.append(main_lists)
            r_lists = main.filter(id=main_lists.id).filter(rasxod__department__user=user)
            r_list = list(r_lists.values('summa'))
            rasxod_list.append(r_list)

            p_lists = main.filter(id=main_lists.id).filter(prixod__department__user=user)
            p_list = list(p_lists.values('summa'))
            prixod_list.append(p_list)
        zipped = zip(main_list, prixod_list, rasxod_list)

        saldo_month_ago = saldo.filter(date_saldo__year=datetime.datetime.today().year).filter(
            date_saldo__month=datetime.datetime.today().month - 1).filter(spravichnik__department__user=user)
        for sal in saldo_month_ago:
            sal_month_ago = Decimal(sal.count_saldo)
            sal_month_ago = float(sal_month_ago)
        r = main.filter(rasxod__department__user=user)
        p = main.filter(prixod__department__user=user)
        for rasxodlar in r:
            print('rasxodlar', rasxodlar.summa)
            rasxod_sum += rasxodlar.summa
        for prixodlar in p:
            print('rasxodlar', prixodlar.summa)
            prixod_sum += prixodlar.summa
        context = {
            'main': zipped,
            'month_ago_saldo': saldo_month_ago,
            'rasxod_sum': rasxod_sum,
            'prixod_sum': prixod_sum,
            'saldo_now': sal_month_ago + prixod_sum - rasxod_sum,
            'today': today_date,
            'deaprtment':department

        }

        response = HttpResponse(
            excel_2(context),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename

        return response


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






