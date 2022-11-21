from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/detail/', views.car_detail, name='detail'),
    path('dealers/', views.dealers, name='dealers'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('faq/', views.faq, name='faq'),

]