from django.contrib import admin
from django.urls import path, include
from administration import views

urlpatterns = [
    path('company', views.view_company, name="view_company"),
]
