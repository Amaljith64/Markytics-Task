from django.urls import path
from account import views


urlpatterns = [

    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),

]