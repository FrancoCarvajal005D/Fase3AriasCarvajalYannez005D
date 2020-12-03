from django.db import models
from django.urls import reverse  		
import uuid  							

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class formulario(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField() 
    message = models.TextField(max_length=250)

    def __str__(self):
        return self.name