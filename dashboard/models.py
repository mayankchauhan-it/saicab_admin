from django.db import models

# Create your models here.
class sliderupdate(models.Model):
    heading = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='slider/')


    def update(self, name, image):
        self.name = name
        self.image = image

        self.save()