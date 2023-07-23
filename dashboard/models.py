from django.db import models

# Create your models here.
class sliderupdate(models.Model):
    heading = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='slider/')


    def update(self, name, image):
        self.name = name
        self.image = image

        self.save()
    




class formdata(models.Model):
    usernamedata = models.CharField(max_length=255, null=True)
    emaildata = models.CharField(max_length=255, null=True)
    pickuplocation = models.CharField(max_length=255, null=True)
    dropofflocation = models.CharField(max_length=255, null=True)
    