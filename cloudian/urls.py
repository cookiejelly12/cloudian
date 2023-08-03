from django.urls import path

from . import views

app_name = 'cloudian'

urlpatterns = [
    path('', views.main, name='main'),
    path('en/', views.main, name='main'),
    path('wc_create/', views.wc_create, name='wc_create'),
    path('en/wc_create/', views.wc_create, name='wc_create'),
    path('<int:img_id>/', views.output, name='wc_output'),
    path('en/<int:img_id>/', views.output, name='wc_output'),
    path('kr/', views.main_kr, name='main_kr'),
    path('kr/wc_create/', views.wc_create_kr, name='wc_create_kr'),
    path('kr/<int:img_id>/', views.output_kr, name='wc_output_kr'),
]