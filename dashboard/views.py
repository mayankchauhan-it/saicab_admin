from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout #For Authentication related modules
from django.contrib import messages

# Email Imports
from django.core.mail import send_mail, EmailMessage
from sai_admin.settings import EMAIL_HOST_USER


# Create your views here.

def dashboard(request):
    # return HttpResponse('<h1>Log In Success</h1>')
    # return render(request, 'dashboard/dashboard2.html')
    return render(request, 'dash/templates/home/index_final.html')
    # return render(request, 'include/base.html')


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


def delete_bookingata(request,id):
    oneway_entry = onewaybooking.objects.get(id=id)
    oneway_entry.delete()

    roundway_entry = roundbooking.objects.get(id=id)
    roundway_entry.delete()

    local_entry = localbooking.objects.get(id=id)
    local_entry.delete()

    messages.success(request,'Data Deleted Successfully!')
    return redirect('bookingentry')

