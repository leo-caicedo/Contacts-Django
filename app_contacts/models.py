# Django
from django.db import models


class Contact(models.Model):

    picture = models.ImageField(upload_to='contacts/picture', blank=True, null=True)

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30, blank=True)

    phone = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100, unique=True, blank=True)

    occupation = models.CharField(max_length=30, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname
