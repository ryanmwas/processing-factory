from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('calculator/', views.calculator, name='calculator'),
    path('login/', views.login, name='login'),
]