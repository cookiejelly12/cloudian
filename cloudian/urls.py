from django.urls import path

from . import views

app_name = 'cloudian'

urlpatterns = [
    path('', views.main, name='main'),
    path('wc_create/', views.wc_create, name='wc_create'),
    path('<int:img_id>/', views.output, name='wc_output'),
    path('en/', views.main_en, name='main_en'),
    path('en/wc_create/', views.wc_create_en, name='wc_create_en'),
    path('en/<int:img_id>/', views.output_en, name='wc_output_en'),
    path('kr/', views.main_kr, name='main_kr'),
    path('kr/wc_create/', views.wc_create_kr, name='wc_create_kr'),
    path('kr/<int:img_id>/', views.output_kr, name='wc_output_kr'),
    path('sp/', views.main_sp, name='main_sp'),
    path('sp/wc_create/', views.wc_create_sp, name='wc_create_sp'),
    path('sp/<int:img_id>/', views.output_sp, name='wc_output_sp'),
]