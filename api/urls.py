from django.contrib import admin
from django.urls import path

import api.views as views 

urlpatterns = [
    path('masters/', views.MastersList.as_view()),
    path('masters/<int:pk>', views.MastersDetail.as_view())
]