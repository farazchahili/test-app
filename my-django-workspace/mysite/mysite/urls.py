from django.contrib import admin
from django.urls import path
from app import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/analyze_run/', views.analyze_run_api, name='analyze_run_api'),
    path('api/get_run_details/', views.get_run_details, name='get_run_details'),
]