from django.urls import path

from . import views

app_name = 'cloudian'

urlpatterns = [
    path('', views.main, name='main'),
    path('wc_create/', views.wc_create, name='wc_create'),
    path('<int:img_id>/', views.output, name='wc_output'),
]