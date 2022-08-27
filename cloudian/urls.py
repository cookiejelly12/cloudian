from django.urls import path

from . import views

app_name = 'cloudian'

urlpatterns = [
    path('', views.text, name='main'),
    path('wc_create/', views.wc_create, name='wc_create'),
]