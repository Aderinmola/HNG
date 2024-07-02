from django.db import models

# Create your models here.

class Ipapp(models.Model):
    client_ip = models.CharField(unique=True, max_length=200)
    location = models.CharField(max_length=200)
    greeting = models.TextField()

    def __str__(self):
        return self.client_ip