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


def formtest(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        # subject = request.POST['subject']
        # usermessage = request.POST['message']

        pickuplocation = request.POST['pickuplocation_name']
        dropofflocation = request.POST['dropofflocation_name']

        obj2 = formdata()
        obj2.usernamedata = username
        obj2.emaildata = email
        obj2.pickuplocation = pickuplocation
        obj2.dropofflocation = dropofflocation
        obj2.save()
    
        # Send the email
        subject = f'New Booking from {username}'
        email_message = f'Name: {username}\nEmail: {email}\nPick-Up Date: {pickuplocation}\nDrop-Off Location: {dropofflocation}'
        
        email = EmailMessage(subject, email_message, to=[EMAIL_HOST_USER])
        email.send()

        return redirect("formtest") 

    return render(request, 'dashboard/formtest.html')

def bookingentry(request):
    form_data = formdata.objects.all()

    return render(request, 'dashboard/formentry.html', {'formdata_list': form_data})

def deletebookingdata(request, id):
    entry = formdata.objects.get(id=id)
    entry.delete()
    messages.success(request,'Data Deleted Successfully!')
    return redirect('bookingentry')