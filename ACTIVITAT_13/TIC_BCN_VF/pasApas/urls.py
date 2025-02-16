from django.urls import path
from . import views

urlpatterns = [
    path('user-form/', views.user_form, name='user_form'),
    path('login-sense-sessio/', views.login_sense_sessio, name='login_sense_sessio'),  # Login sense sessió
    path('login-amb-sessio/', views.login_amb_sessio, name='login_amb_sessio'),
]