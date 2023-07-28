from django.db import models

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


class formdata(models.Model):
    usernamedata = models.CharField(max_length=255, null=True)
    emaildata = models.CharField(max_length=255, null=True)
    pickuplocation = models.CharField(max_length=255, null=True)
    dropofflocation = models.CharField(max_length=255, null=True)


class onewaybooking(models.Model):
    user_name = models.CharField(max_length=255, null=True)
    user_email = models.CharField(max_length=255, null=True)
    pickuplocation = models.CharField(max_length=255, null=True)
    dropofflocation = models.CharField(max_length=255, null=True)
    pickup_date = models.CharField(max_length=255,null=True)