from django.urls import path
from . import views

urlpatterns = [
    path('user-form/', views.user_form, name='user_form'),
    path('login-form/', views.login_sense_sessio, name='login_form'),
]