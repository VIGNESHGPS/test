from django.contrib import admin
from django.urls import path
from . import views
from .views import study_list, add_study, delete_study, edit_study

urlpatterns = [
    path('', views.study_list, name='study_list'),
    path('add/', views.add_study, name='add_study'),
    path('delete/<int:pk>/', views.delete_study, name='delete_study'),
    path('edit/<int:pk>/', views.edit_study, name='edit_study'),
    path('delete-multiple/', views.delete_multiple_studies, name='delete_multiple_studies'),
    path('view/<int:pk>/', views.view_study, name='view_study'),
]

