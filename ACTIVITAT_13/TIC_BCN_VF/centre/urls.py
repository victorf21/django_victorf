from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.professors , name='teachers'),
    path('students/', views.alumnat , name='students'),
    path('students/<str:pk>/', views.alumnat , name='students'),
    path('teachers/<str:pk>/', views.alumnat , name='teachers'),
]