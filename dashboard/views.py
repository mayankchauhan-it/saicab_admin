from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout #For Authentication related modules
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views import View

# Email Imports
from django.core.mail import send_mail, EmailMessage
from sai_admin.settings import EMAIL_HOST_USER


# Create your views here.

def dashboard(request):
    return render(request, 'dash/templates/home/index_final.html')


def loginpage(request):
    if request.method == "POST":
        email = request.POST.get('user')
        password = request.POST.get('pass')
        print(email, password)

        user  = authenticate(request, username = email, password = password)

        if user is not None:
            login(request, user)
            # Redirect to a success page or do further processing
            return redirect('dashboard')
        else:
            # Authentication failed, handle the error
            return render(request, 'dashboard/login.html', {'error': 'Invalid credentials'})


    return render(request, 'dashboard/login.html')


def home(request):
    print(request.FILES)
    if request.method == 'POST':
        heading_text1 = request.POST.get('headingname1')
        heading_text2 = request.POST.get('headingname2')
        image_file = request.FILES.get('myfile')

        obj = sliderupdate()
        obj.heading = heading_text1
        obj.heading2 = heading_text2

        if image_file:
            obj.image = image_file
        obj.save()

        return redirect('home')

    heading_content = sliderupdate.objects.all()

    return render(request, 'dashboard/home.html', {'heading_data': heading_content})

def deletehomedata(request, id):
    entry = sliderupdate.objects.get(id=id)
    # entry = sliderupdate.objects.all()
    entry.delete()
    messages.success(request,'Data Deleted Successfully!')
    return redirect('home')


def bookingentry(request):
    onewaybooking_data = onewaybooking.objects.all()
    roundbooking_data = roundbooking.objects.all()
    localbooking_data = localbooking.objects.all()
    return render(request, 'dashboard/formentry.html', {'onewaybooking_data': onewaybooking_data,'roundbooking_data': roundbooking_data,'localbooking_data': localbooking_data })


def Delete_singleTrip_entry(request, id):
    singleTrip_entry = onewaybooking.objects.get(id=id)
    singleTrip_entry.delete()

    messages.success(request, 'Data Deleted Successfully from Oneway Booking!')
    return redirect('bookingentry')

def Delete_roundTrip_entry(request, id):
    roundTrip_entry = roundbooking.objects.get(id=id)
    roundTrip_entry.delete()
    messages.success(request, 'Data Deleted Successfully from Roundway Booking!')
    return redirect('bookingentry')

def Delete_localTrip_entry(request, id):
    localTrip_entry = localbooking.objects.get(id=id)
    localTrip_entry.delete()
    messages.success(request, 'Data Deleted Successfully from Local Booking!')
    return redirect('bookingentry')




