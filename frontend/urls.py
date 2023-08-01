from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.frontend, name="Front End"),
    path('oneway_view', views.form_oneway, name='form_oneway'),
    path('roundway_view', views.form_roundway, name='form_roundway'),
    path('localway_view', views.form_localway, name='form_localway'),
    path('get-states-and-cities/', views.get_cities_for_state, name='get_cities_for_state'),
    path('about', views.about_front, name='aboutus'),
    path('services', views.service_front, name='services'),
    path('gallery', views.gallery_front, name='gallery'),
    path('contactus', views.contact_front, name='contact_us'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)