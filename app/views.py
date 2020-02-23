from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from app.model import Department, Spravichnik, Main


class DepartmentListView(TemplateView):
    template_name = 'department/list.html'

    def get_context_data(self, **kwargs):
        dept = Department.objects.all()
        context = {
            'department': dept

        }
        return context


class DepartmentCreateView(TemplateView):
    template_name = 'department/create.html'


class DepartmentUpdateView(DetailView):
    template_name = 'department/update.html'
    pk_url_kwarg = 'id'
    queryset = Department.objects.all()
    context_object_name = 'department'


class SpravichnikListView(TemplateView):
    template_name = 'spravichnik/list.html'

    def get_context_data(self, **kwargs):
        dept = Department.objects.all()
        sp = Spravichnik.objects.all()
        context = {
            'depts': dept,
            'sprav': sp

        }
        return  context


class SpravichnikUpdateView(DetailView):
    template_name = 'spravichnik/update.html'
    pk_url_kwarg = 'id'
    queryset = Spravichnik.objects.all()
    context_object_name = 'spravchnik'

    def get_context_data(self, **kwargs):
        context = super(SpravichnikUpdateView, self).get_context_data(**kwargs)
        context['dep'] = Department.objects.all()
        return context


class SpravichnikCreateView(TemplateView):
    template_name = 'spravichnik/create.html'

    def get_context_data(self, **kwargs):
        det = Department.objects.all()
        context = {
            'depts': det

        }
        return context


class MainListView(TemplateView):
    template_name = 'main/list.html'

    def get_context_data(self, **kwargs):
        m = Main.objects.all()
        context = {
            'main': m
        }
        return context


class MainUpdateView(DetailView):
    template_name = 'main/update.html'
    context_object_name = 'main'
    pk_url_kwarg = 'id'
    queryset = Main.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MainUpdateView, self).get_context_data(**kwargs)
        context['spr'] = Spravichnik.objects.all()
        return context


class MainCreateView(TemplateView):
    template_name = 'main/create.html'

    def get_context_data(self, **kwargs):
        m = Main.objects.all()
        sp = Spravichnik.objects.all()
        context = {
            'main': m,
            'spr': sp
        }
        return context


class



