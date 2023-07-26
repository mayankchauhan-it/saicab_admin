from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from dashboard.models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout #For Authentication related modules
from django.contrib import messages

# Email Imports
from django.core.mail import send_mail, EmailMessage
from sai_admin.settings import EMAIL_HOST_USER


from django.http import JsonResponse
from geopy.geocoders import Nominatim


def get_cities_for_state(request):
    query = request.GET.get('query', '')
    
    # Create a geolocator object
    geolocator = Nominatim(user_agent="myGeocoder")
    
    # Use geopy to get the location for the query
    location = geolocator.geocode(query + ", India", exactly_one=False)
    
    data = []
    if location:
        # Extract the state and city names from the location data
        for loc in location:
            address = loc.raw['display_name'].split(",")
            state = address[-3].strip()
            city = address[0].strip()
            data.append(city + ", " + state)
    
    return JsonResponse(data, safe=False)


def frontend(request):
    obj = sliderupdate.objects.all()
    heading_content = ""
    heading_content2 = ""


    if obj.__len__() != 0:
        # Check if the queryset is not empty before accessing the latest object
        latest_obj = obj.latest('id')
        heading_content = latest_obj.heading
        print(heading_content)
        heading_content2 = latest_obj.heading2

    return render(request, 'frontend/home_front.html', {'latest_heading': heading_content, 'latest_heading2': heading_content2})

def form_oneway(request):
    if request.method == "POST":
        yourname = request.POST.get('yourname')
        youremail = request.POST.get('youremail')
        pickup = request.POST.get('pickup')
        dropoff = request.POST.get('dropoff')
        date = request.POST.get('date')
        time = request.POST.get('time')
        totalprice = request.POST.get('total')
        firstname = request.POST.get('firstname')
        lasttname = request.POST.get('lasttname')
        emailid = request.POST.get('emailid')
        phonenumber = request.POST.get('phonenumber')
        comment = request.POST.get('comment')
        
        print(f"{yourname}\n{youremail}\n{pickup}\n{dropoff}\n{date}\n{time}\n{totalprice}\n{firstname}\n{lasttname}\n{emailid}\n{phonenumber}\n{comment}")


         # Send the email
        subject = f"New Booking from {yourname}"
        email_message = f"""Name: <strong>{yourname}</strong> <br>Email: <strong>{youremail}</strong> <br>Pick-Up Locaiton: <strong>{pickup}</strong><br>Drop-Off Location: <strong>{dropoff}</strong><br>Pick-Up Date: <strong>{date}</strong><br>Pick-Up Time: <strong>{time}<br></strong>Total Price: <strong>{totalprice}</strong>"""

        email = EmailMessage(subject, email_message, to=[EMAIL_HOST_USER])
        email.content_subtype = "html"
        email.send()

    return render (request, 'frontend/index.html')


def form_roundway(request):
    if request.method == "POST":
        yourname = request.POST.get('yourname')
        youremail = request.POST.get('youremail')
        pickup = request.POST.get('pickup')
        dropoff = request.POST.get('dropoff')
        pickupdate = request.POST.get('pickupdate')
        pickuptime = request.POST.get('pickuptime')
        dropoffdate = request.POST.get('dropoffdate')
        dropofftime = request.POST.get('dropofftime')
        totalprice = request.POST.get('total')
        firstname = request.POST.get('firstname')
        lasttname = request.POST.get('lasttname')
        emailid = request.POST.get('emailid')
        phonenumber = request.POST.get('phonenumber')
        comment = request.POST.get('comment')
        
        print(f"{yourname}\n{youremail}\n{pickup}\n{dropoff}\n{pickupdate}\n{pickuptime}\n{totalprice}\n{firstname}\n{lasttname}\n{emailid}\n{phonenumber}\n{comment}")


         # Send the email
        subject = f"New Booking from {yourname}"
        email_message = f"""Name: <strong>{yourname}</strong> <br>Email: <strong>{youremail}</strong> <br>Pick-Up Locaiton: <strong>{pickup}</strong><br>Drop-Off Location: <strong>{dropoff}</strong><br>Pick-Up Date: <strong>{pickupdate}</strong><br>Pick-Up Time: <strong>{pickuptime}</strong><br> Drop-Off Date: <strong>{dropoffdate}</strong><br>Drop-Off Time: <strong>{dropofftime}<br></strong>Total Price: <strong>{totalprice}</strong>"""

        email = EmailMessage(subject, email_message, to=[EMAIL_HOST_USER])
        email.content_subtype = "html"
        email.send()


    return render (request, 'frontend/index.html')


def form_localway(request):
    if request.method == "POST":
        yourname = request.POST.get('yourname')
        youremail = request.POST.get('youremail')
        location = request.POST.get('yourlocation')
        hour = request.POST.get('hour')
        
        print(f"{yourname}\n{youremail}\n{location}\n{hour}\n")


         # Send the email
        subject = f"New Booking from {yourname}"
        email_message = f"""Name: <strong>{yourname}</strong> <br>Email: <strong>{youremail}</strong> <br>Locaiton: <strong>{location}</strong><br>Hour: <strong>{hour}</strong><br>"""

        email = EmailMessage(subject, email_message, to=[EMAIL_HOST_USER])
        email.content_subtype = "html"
        email.send()

    return render (request, 'frontend/index.html')


def about(request):

    # return render(request, 'frontend/about.html')
    return render(request, 'frontend/about_front.html')
