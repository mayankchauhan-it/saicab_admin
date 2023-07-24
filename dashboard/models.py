from django.db import models

# Create your models here.
class sliderupdate(models.Model):
    heading = models.CharField(max_length=255, null=True)
    heading2 = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='slider/', blank=True, null=True)


    def update(self, name1, name2, image):
        self.name = name1
        self.name2 = name2
        self.image = image

        self.save()
    




class formdata(models.Model):
    usernamedata = models.CharField(max_length=255, null=True)
    emaildata = models.CharField(max_length=255, null=True)
    pickuplocation = models.CharField(max_length=255, null=True)
    dropofflocation = models.CharField(max_length=255, null=True)
    