from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout #For Authentication related modules
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
import json

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


def aboutus(request):
    if request.method == 'POST':
        about_heading = request.POST.get('heading_name')
        about_desc1 = request.POST.get('description_name')
        about_desc2 = request.POST.get('description2_name')
        vision = request.POST.get('vision_name')
        mission = request.POST.get('mission_name')
        image_file = request.FILES.get('about_iamge')


        obj = about()
        # obj.about_title = json.dumps(full_heading)  # Convert to JSON string
        obj.about_title = about_heading
        obj.about_desc1 = about_desc1
        obj.about_desc2 = about_desc2
        obj.vision = vision
        obj.mission = mission

        if image_file:
            obj.image = image_file
        obj.save()

        return redirect('add_aboutus')

    about_content = about.objects.all()


    return render(request, 'dashboard/about_admin.html', {'about_data': about_content})

def gallery(request):
    if request.method == 'POST':
        gallery_city = request.POST.get('city_name')
        gellery_description = request.POST.get('description_name')
        gallery_image_file = request.FILES.get('gallery_iamge_name')

        obj = gallery_data()
        obj.city = gallery_city
        obj.description = gellery_description

        if gallery_image_file:
            obj.gallery_image = gallery_image_file
        obj.save()

        return redirect('admin_gallery')

    gallery_content = gallery_data.objects.all()

    # Number of items to show per page
    items_per_page = 5

    # Create a Paginator object
    paginator = Paginator(gallery_content, items_per_page)

    # Get the current page number from the request
    page_number = request.GET.get('page')

    # Get the Page object for the requested page number
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard/gallery_admin.html', {'gallery_data_list': gallery_content, 'page_obj': page_obj})

def services(request):
    if request.method == 'POST':
        service_heading = request.POST.get('service_name')
        service_desc1 = request.POST.get('description_name')
        service_image_file = request.FILES.get('service_image_name')

        obj = services_data()
        obj.service_Name = service_heading
        obj.service_Description = service_desc1

        if service_image_file:
            obj.service_image = service_image_file
        obj.save()

        return redirect('admin_services')

    service_content = services_data.objects.all()

    # Number of items to show per page
    items_per_page = 5

    # Create a Paginator object
    paginator = Paginator(service_content, items_per_page)

    # Get the current page number from the request
    page_number = request.GET.get('page')

    # Get the Page object for the requested page number
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard/service_admin.html', {'service_data': service_content, 'page_obj': page_obj})

def contact(request):
    if request.method == 'POST':
        contact_address = request.POST.get('address_name')
        contact_email = request.POST.get('email_name')
        contact_mobile = request.POST.get('mobile_name')

        obj = contactus()
        obj.contact_Address = contact_address
        obj.contact_Email = contact_email
        obj.contact_Mobile = contact_mobile

        obj.save()

        return redirect('admin_contact')

    contact_content = contactus.objects.all()

    # Number of items to show per page
    items_per_page = 3

    # Create a Paginator object
    paginator = Paginator(contact_content, items_per_page)

    # Get the current page number from the request
    page_number = request.GET.get('page')

    # Get the Page object for the requested page number
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard/contact_admin.html', {'contact_data': contact_content, 'page_obj': page_obj})


def add_car(request):
    if request.method == 'POST':
        car_name = request.POST.get('carName_name')
        seating_capacity = request.POST.get('seatingCapacity_name')
        car_rate = request.POST.get('carRate_name')
        car_range = request.POST.get('carRange_name')
        driver_allowance = request.POST.get('driverAllowance_name')
        image_file = request.FILES.get('carImage_name')

        obj = cars()
        obj.car_name = car_name
        obj.seating_capacity = seating_capacity
        obj.rate_par_km = car_rate
        obj.min_range = car_range
        obj.driver_allowance = driver_allowance

        if image_file:
            obj.car_image = image_file
        obj.save()

        return redirect('add_car')

    car_data = cars.objects.all()

    # Number of items to show per page
    items_per_page = 3

    # Create a Paginator object
    paginator = Paginator(car_data, items_per_page)

    # Get the current page number from the request
    page_number = request.GET.get('page')

    # Get the Page object for the requested page number
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard/cars.html', {'car_data': car_data, 'page_obj': page_obj})
    # return render(request, 'dashboard/cars.html')

def add_ride(request):
    if request.method == 'POST':
        ride_starting_location = request.POST.get('startLocation_name')
        ride_ending_location = request.POST.get('endLocation_name')
        ride_Type = request.POST.get('rideType_name')
        sedan_Price = request.POST.get('sendaPrice_name')
        suv_Price = request.POST.get('suvPrice_name')

        obj = rides()
        obj.ride_start = ride_starting_location
        obj.ride_end = ride_ending_location
        obj.ride_type = ride_Type
        obj.sedan_price = sedan_Price
        obj.suv_price = suv_Price
        obj.save()

        return redirect('add_ride')

    ride_Data = rides.objects.all()

    # Number of items to show per page
    items_per_page = 3

    # Create a Paginator object
    paginator = Paginator(ride_Data, items_per_page)

    # Get the current page number from the request
    page_number = request.GET.get('page')

    # Get the Page object for the requested page number
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard/cars_rides.html', {'ride_Data': ride_Data, 'page_obj': page_obj})


def delete_Ride(request, id):
    car = rides.objects.get(id=id)
    # entry = sliderupdate.objects.all()
    car.delete()
    return redirect('add_ride')

def delete_car(request, id):
    car = cars.objects.get(id=id)
    # entry = sliderupdate.objects.all()
    car.delete()
    return redirect('add_car')

def delete_about(request, id):
    car = about.objects.get(id=id)
    # entry = sliderupdate.objects.all()
    car.delete()
    return redirect('add_aboutus')


def delete_gallery(request, id):
    car = gallery_data.objects.get(id=id)
    # entry = sliderupdate.objects.all()
    car.delete()
    return redirect('admin_gallery')

def delete_service(request, id):
    car = services_data.objects.get(id=id)
    # entry = sliderupdate.objects.all()
    car.delete()
    return redirect('admin_services')

def delete_contact(request, id):
    car = contactus.objects.get(id=id)
    # entry = sliderupdate.objects.all()
    car.delete()
    return redirect('admin_contact')

def deletehomedata(request, id):
    entry = sliderupdate.objects.get(id=id)
    # entry = sliderupdate.objects.all()
    entry.delete()
    return redirect('home')

def bookingentry(request):
    onewaybooking_data = onewaybooking.objects.all()
    roundbooking_data = roundbooking.objects.all()
    localbooking_data = localbooking.objects.all()
    return render(request, 'dashboard/formentry.html', {'onewaybooking_data': onewaybooking_data,'roundbooking_data': roundbooking_data,'localbooking_data': localbooking_data })

def Delete_singleTrip_entry(request, id):
    singleTrip_entry = onewaybooking.objects.get(id=id)
    singleTrip_entry.delete()

    return redirect('bookingentry')

def Delete_roundTrip_entry(request, id):
    roundTrip_entry = roundbooking.objects.get(id=id)
    roundTrip_entry.delete()
    return redirect('bookingentry')

def Delete_localTrip_entry(request, id):
    localTrip_entry = localbooking.objects.get(id=id)
    localTrip_entry.delete()
    return redirect('bookingentry')




def update_about(request, id):
    entry = get_object_or_404(about, id = id)

    if request.method == 'POST':
        entry.about_title = request.POST.get('headingNameUpdate')
        entry.about_desc1 = request.POST.get('aboutdesc1update')
        entry.about_desc2 = request.POST.get('aboutdesc2update')
        entry.vision = request.POST.get('aboutVisionUpdate')
        entry.mission = request.POST.get('aboutMissionUpdate')


        image_entry = request.FILES.get('aboutImageUpdate')
        if image_entry:
            entry.image.save(image_entry.name, image_entry, save=True)
        entry.save()
    
    return redirect('add_aboutus')


def update_contact(request, id):
    entry = get_object_or_404(contactus, id=id)

    if request.method == 'POST':
        entry.contact_Address = request.POST.get('addressupdate')
        entry.contact_Email = request.POST.get('emailupdate')
        entry.contact_Mobile = request.POST.get('mobileupdate')
        entry.save()
    
    return redirect('admin_contact')


def update_gallery(request, id):
    entry = get_object_or_404(gallery_data, id=id)

    if request.method == 'POST':
        entry.city = request.POST.get('cityupdate')
        entry.description = request.POST.get('descupdate')

        image_var = request.FILES.get('gallery_image')
        if image_var:
            entry.gallery_image.save(image_var.name, image_var, save=True)
        entry.save()
    
    return redirect('admin_gallery')


def update_services(request, id):
    entry = get_object_or_404(services_data, id=id)

    if request.method == 'POST':
        entry.service_Name = request.POST.get('serviceNameUpdate')
        entry.service_Description = request.POST.get('Servicedescupdate')

        image_var = request.FILES.get('service_image')
        if image_var:
            entry.service_image.save(image_var.name, image_var, save=True)
        entry.save()

    
    return redirect('admin_services')

def update_rides(request, id):
    entry = get_object_or_404(rides, id=id)

    if request.method == 'POST':
        entry.ride_start = request.POST.get('rideStartLocationUpdate_name')
        entry.ride_end = request.POST.get('rideEndLocationUpdate_name')
        entry.ride_type = request.POST.get('rideTypeUpdate_name')
        entry.sedan_price = request.POST.get('sendaPriceUpdate_name')
        entry.suv_price = request.POST.get('suvPriceUpdate_name')
        entry.save()


    
    return redirect('add_ride')


def update_cars(request, id):
    entry = get_object_or_404(cars, id=id)

    if request.method == 'POST':
        entry.car_name = request.POST.get('updatecarName_name')
        entry.seating_capacity = request.POST.get('updateseatingCapacity_name')
        entry.rate_par_km = request.POST.get('updatecarRate_name')
        entry.min_range = request.POST.get('updatecarRange_name')
        entry.driver_allowance = request.POST.get('updatedriverAllowance_name')

        image_var = request.FILES.get('updatecarImage_name')
        if image_var:
            entry.car_image.save(image_var.name, image_var, save=True)
        entry.save()
    
    return redirect('add_car')
