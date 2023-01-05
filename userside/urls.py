from django.urls import path
from userside import views


urlpatterns = [

    path('submit_form', views.SubmitForm, name='submit_form'),

]
