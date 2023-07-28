from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.loginpage, name = 'login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('home', views.home, name='home'),
    path('homedatadelete/<int:id>', views.deletehomedata, name='deletehome'),
    path('bookingentry', views.bookingentry, name='bookingentry'),
    # path('deletebookingentry/<int:id>', views.delete_bookingata, name='deleteformdata'),
    path('delete_singleTrip_entry/<int:id>/', views.Delete_singleTrip_entry, name='Delete_singleTrip_entry'),
    path('delete_roundTrip_entry/<int:id>/', views.Delete_roundTrip_entry, name='Delete_roundTrip_entry'),
    path('delete_localTrip_entry/<int:id>/', views.Delete_localTrip_entry, name='Delete_localTrip_entry'),




] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
