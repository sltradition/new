
from django.urls import path

from functions import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout')

]