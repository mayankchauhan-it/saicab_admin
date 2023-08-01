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
    
    cars_list = cars.objects.all()

    return render(request, 'page/home_front.html', {'latest_heading': heading_content, 'latest_heading2': heading_content2, "car_data":cars_list})

def form_oneway(request):
    if request.method == "POST":
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
        
        form_obj = onewaybooking()
        form_obj.user_name = f"{firstname} {lasttname}"
        form_obj.user_email = emailid
        form_obj.pickuplocation = pickup
        form_obj.dropofflocation = dropoff
        form_obj.pickup_date = date
        form_obj.save()

         # Send the email
        subject = f"New Booking from {firstname} {lasttname}"
        email_message = f"""Name: <strong>{firstname} {lasttname}</strong> <br>Email: <strong>{emailid}</strong> <br>Pick-Up Locaiton: <strong>{pickup}</strong><br>Drop-Off Location: <strong>{dropoff}</strong><br>Pick-Up Date: <strong>{date}</strong><br>Pick-Up Time: <strong>{time}<br></strong>Total Price: <strong>{totalprice}</strong>"""

        email = EmailMessage(subject, email_message, to=[EMAIL_HOST_USER])
        email.content_subtype = "html"
        email.send()

        return redirect('Front End')

    return render (request, 'page/home_front.html')


def form_roundway(request):
    if request.method == "POST":
        pickup = request.POST.get('pickup')
        dropoff = request.POST.get('dropoff')
        pickupdate = request.POST.get('pickupdate')
        pickuptime = request.POST.get('pickuptime')
        dropoffdate = request.POST.get('dropoffdate')
        dropofftime = request.POST.get('dropofftime')
        totalprice = request.POST.get('total')
        firstname = request.POST.get('firstname')
        lasttname = request.POST.get('lastname')
        emailid = request.POST.get('emailid')
        phonenumber = request.POST.get('phonenumber')
        comment = request.POST.get('comment')


        form_obj = roundbooking()
        form_obj.user_name = f"{firstname} {lasttname}"
        form_obj.user_email = emailid
        form_obj.pickuplocation = pickup
        form_obj.dropofflocation = dropoff
        form_obj.pickup_date = pickupdate
        form_obj.pickup_time = pickuptime
        form_obj.dropoff_date = dropoffdate
        form_obj.dropoff_time = dropofftime
        form_obj.save()
        
         # Send the email
        subject = f"New Booking from {firstname} {lasttname}"
        email_message = f"""Name: <strong>{firstname} {lasttname}</strong> <br>Email: <strong>{emailid}</strong> <br>Pick-Up Locaiton: <strong>{pickup}</strong><br>Drop-Off Location: <strong>{dropoff}</strong><br>Pick-Up Date: <strong>{pickupdate}</strong><br>Pick-Up Time: <strong>{pickuptime}</strong><br> Drop-Off Date: <strong>{dropoffdate}</strong><br>Drop-Off Time: <strong>{dropofftime}<br></strong>Total Price: <strong>{totalprice}</strong>"""

        email = EmailMessage(subject, email_message, to=[EMAIL_HOST_USER])
        email.content_subtype = "html"
        email.send()

        return redirect('Front End')


    return render (request, 'page/home_front.html')


def form_localway(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        youremail = request.POST.get('youremail')
        location = request.POST.get('yourlocation')
        hour_required = request.POST.get('hour')

        form_obj = localbooking()
        form_obj.user_name = f"{firstname} {lastname}"
        form_obj.user_email = youremail
        form_obj.pickuplocation = location
        form_obj.hour = hour_required
        form_obj.save()
        
         # Send the email
        subject = f"New Booking from {firstname} {lastname}"
        email_message = f"""Name: <strong> {firstname}{lastname}</strong> <br>Email: <strong>{youremail}</strong> <br>Hour: <strong>{location}</strong><br>Hour: <strong>{hour_required}</strong><br>"""

        email = EmailMessage(subject, email_message, to=[EMAIL_HOST_USER])
        email.content_subtype = "html"
        email.send()
        
        return redirect('Front End')

    return render (request, 'page/home_front.html')


def about_front(request):
    about_obj = about.objects.all()
    # return render(request, 'frontend/about.html')
    return render(request, 'page/about_front.html', {'about_list': about_obj})


def service_front(request):
    service_obj = services_data.objects.all()

    # return render(request, 'frontend/service.html')
    return render(request, 'page/service_front.html', {'service_data': service_obj})

def gallery_front(request):

    gallery_obj = gallery_data.objects.all()

    # return render(request, 'frontend/gallery.html')
    return render(request, 'page/gallery_front.html', {'gallery_data': gallery_obj})

def contact_front(request):

    contact_obj = contactus.objects.all()

    # return render(request, 'frontend/contact.html')
    return render(request, 'page/contact_front.html', {'contact_data': contact_obj})