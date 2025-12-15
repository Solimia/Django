from django.contrib import admin
from django.urls import path

import Beauty.views

urlpatterns = [
    path('', Beauty.views.list),
    path('<int:pk>/', Beauty.views.detail),
]