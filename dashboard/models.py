from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class sliderupdate(models.Model):
    heading = models.CharField(max_length=255, null=True)
    heading2 = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='slider/', null=True, blank=True)


    def update(self, new_heading, new_heading2, new_image=None):
        self.heading = new_heading
        self.heading2 = new_heading2

        if new_image:
            self.image = new_image

        self.save()

class onewaybooking(models.Model):
    user_name = models.CharField(max_length=255, null=True)
    user_email = models.CharField(max_length=255, null=True)
    pickuplocation = models.CharField(max_length=255, null=True)
    dropofflocation = models.CharField(max_length=255, null=True)
    pickup_date = models.CharField(max_length=255,null=True)
    pickup_time = models.CharField(max_length=255, null=True)

class roundbooking(models.Model):
    user_name = models.CharField(max_length=255, null=True)
    user_email = models.CharField(max_length=255, null=True)
    pickuplocation = models.CharField(max_length=255, null=True)
    dropofflocation = models.CharField(max_length=255, null=True)
    pickup_date = models.CharField(max_length=255,null=True)
    pickup_time = models.CharField(max_length=255, null=True)
    dropoff_date = models.CharField(max_length=255,null=True)
    dropoff_time = models.CharField(max_length=255, null=True)
    
class localbooking(models.Model):
    user_name = models.CharField(max_length=255, null=True)
    user_email = models.CharField(max_length=255, null=True)
    pickuplocation = models.CharField(max_length=255, null=True)
    hour = models.CharField(max_length=255, null=True)

class cars(models.Model):
    car_name = models.CharField(max_length=255, null=True)
    seating_capacity = models.IntegerField(null=True)
    rate_par_km = models.IntegerField(null=True)
    min_range = models.IntegerField(null=True)
    driver_allowance = models.IntegerField(null=True)
    car_image = models.ImageField(upload_to='carImage/', null=True, blank=True)

class rides(models.Model):
    ride_start = models.CharField(max_length=255, null=True)
    ride_end = models.CharField(max_length=255, null=True)
    ride_type = models.CharField(max_length=255, null=True)
    sedan_price = models.IntegerField(null=True)
    suv_price = models.IntegerField(null=True)

class about(models.Model):
    about_title = models.CharField(max_length=255, null=True)
    about_desc1 = RichTextField(max_length=1000, null=True)
    about_desc2 = models.TextField(null=True)
    vision = models.CharField(max_length=500, null=True)
    mission = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='about/', null=True, blank=True)

    def update(self, title, Description, description2, vission, mission, image):
        self.id = id
        self.about_title = title
        self.about_desc1 = Description
        self.about_desc2 = description2
        self.vision = vission
        self.mission = mission
        self.image = image
        self.save()

class gallery_data(models.Model):
    city = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=1000, null=True)
    gallery_image = models.ImageField(upload_to='gallery/', null=True, blank=True)


    def update(self, new_city, new_description, new_gallery_image=None):
        self.city = new_city
        self.description = new_description

        if new_gallery_image:
            self.gallery_image = new_gallery_image

        self.save()


class services_data(models.Model):
    service_Name = models.CharField(max_length=255, null=True)
    service_Description = models.CharField(max_length=1000, null=True)
    service_image = models.ImageField(upload_to='service/', null=True, blank=True)

    def update(self, new_service, new_description, new_gallery_image=None):
        self.service_Name = new_service
        self.service_Description = new_description

        if new_gallery_image:
            self.gallery_image = new_gallery_image

        self.save()




class contactus(models.Model):
    contact_Address = models.CharField(max_length=255, null=True)
    contact_Email = models.EmailField(max_length=255, null=True)
    contact_Mobile = models.IntegerField(null=True)


    def update(self, address, email, mobile):
        self.id = id
        self.about_title = address
        self.about_desc1 = email
        self.about_desc2 = mobile
        self.save()


class contact_Form(models.Model):
    contactName = models.CharField(max_length=255, null=True)
    contactEmail = models.EmailField(null=True)
    contactPhone = models.IntegerField(null=True)
    contactSubject = models.CharField(max_length=500, null=True)
    contactMessage = models.CharField(max_length=500, null=True)