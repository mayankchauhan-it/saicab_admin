from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.loginpage, name = 'login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('home', views.home, name='home'),
    path('cars', views.add_car, name='add_car'),
    path('rides', views.add_ride, name='add_ride'),
    path('aboutus', views.aboutus, name='add_aboutus'),
    path('gallery', views.gallery, name='admin_gallery'),
    path('services', views.services, name='admin_services'),
    path('contact', views.contact, name='admin_contact'),
    path('DeleteRide/<int:id>/', views.delete_Ride, name='delete_Ride'),
    path('DeleteCar/<int:id>/', views.delete_car, name='delete_car'),
    path('DeleteAbout/<int:id>/', views.delete_about, name='delete_about'),

    path('DeleteGallery/<int:id>/', views.delete_gallery, name='delete_gallery'),
    path('DeleteService/<int:id>/', views.delete_service, name='delete_service'),
    path('DeleteContact/<int:id>/', views.delete_contact, name='delete_contact'),




    path('homedatadelete/<int:id>', views.deletehomedata, name='deletehome'),
    path('bookingentry', views.bookingentry, name='bookingentry'),
    path('delete_singleTrip_entry/<int:id>/', views.Delete_singleTrip_entry, name='Delete_singleTrip_entry'),
    path('delete_roundTrip_entry/<int:id>/', views.Delete_roundTrip_entry, name='Delete_roundTrip_entry'),
    path('delete_localTrip_entry/<int:id>/', views.Delete_localTrip_entry, name='Delete_localTrip_entry'),




] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
