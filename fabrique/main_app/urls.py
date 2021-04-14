from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'main_app'

urlpatterns = [
    path('survey/', views.SurveyListView.as_view()),
    path('survey/<int:pk>/', views.SurveyDetailView.as_view()),
    path('response/', views.ResponseCreateView.as_view()),
    path('get-responses/', views.ResponseView.as_view()),
]
