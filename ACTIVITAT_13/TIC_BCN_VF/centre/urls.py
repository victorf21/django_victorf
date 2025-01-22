from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.professors , name='proff'),
    path('students/', views.alumnat , name='students'),
]