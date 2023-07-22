from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout #For Authentication related modules
from django.contrib import messages

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

    if request.method == 'POST':
        heading_text = request.POST['headingname']
        image_file = request.FILES['File']

        obj = sliderupdate()
        obj.heading = heading_text
        obj.image = image_file
        obj.save()

    heading_content = sliderupdate.objects.all()


    return render (request, 'dashboard/home.html', {'heading_data' : heading_content})

def deletehomedata(request, id):
    entry = sliderupdate.objects.get(id=id)
    entry.delete()
    messages.success(request,'Data Deleted Successfully!')
    return redirect('home')