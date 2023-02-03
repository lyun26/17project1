# addtion code file

from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes)
]