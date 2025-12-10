from django.contrib import admin
from django.urls import path

import Beauty.views

urlpatterns = [
    path('list', Beauty.views.list),
    path('<int:pk>/', Beauty.views.detail),
]