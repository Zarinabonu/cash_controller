"""cash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.api.urls')),
    path('department/list', views.DepartmentListView.as_view(), name='department-list'),
    path('department/create', views.DepartmentCreateView.as_view(), name='department-create'),
    path('department/update/<int:id>', views.DepartmentUpdateView.as_view(), name='department-update'),
    path('spravichnik/list', views.SpravichnikListView.as_view(), name='spravichnik-list'),
    path('spravichnik/create', views.SpravichnikCreateView.as_view(), name='spravichnik-create'),
    path('spravichnik/update/<int:id>', views.SpravichnikUpdateView.as_view(), name='spravichnik-update'),
    path('rasxod/list', views.MainListView.as_view(), name='rasxod-list'),
    path('rasxod/update/<int:id>', views.RasxodUpdateView.as_view(), name='rasxod-update'),
    path('rasxod/create', views.RasxodCreateView.as_view(), name='rasxod-create'),
    path('saldo/create', views.SaldoCreateView.as_view(), name='saldo-create'),
    path('saldo', views.SaldoListView.as_view(), name='saldo-list'),
    path('', views.Login.as_view(), name='login'),
    path('logout', views.LogOut.as_view(), name='logout'),
    path('prixod/list', views.IncomeListView.as_view(), name='prixod-list'),
    path('prixod/update/<int:id>', views.IncomeUpdateView.as_view(), name='prixod-update'),
    path('prixod/create', views.IncomeCreateView.as_view(), name='prixod-create'),
    path('statistica', views.StatisticaView.as_view(), name='statistica'),
    path('excel', views.ExcelView.as_view(), name='excel'),

]
