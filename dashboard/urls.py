from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.loginpage, name = 'login'),
    path('dashboard/', views.dashboard, name='dashboard'),












] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
