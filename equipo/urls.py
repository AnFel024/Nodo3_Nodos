from django.contrib import admin
from django.urls import path, include
from rest_framework import views

from equipo.views import getNodoValue, setNodoValue, sumaNodos

urlpatterns = [
    path('getValue/', getNodoValue.as_view(), name='getNodoValue'),
    path('setValue/<int:value>/', setNodoValue.as_view(), name='setNodoValue'),
    path('sumaNodos/', sumaNodos.as_view(), name='sumaNodos'),
]
