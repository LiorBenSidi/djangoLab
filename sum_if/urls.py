from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sum_if', views.sum_if, name='sum_if')
]
