from django.contrib import admin
from django.urls import path
from analitica import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('home/', views.dashboard, name='home'),
]