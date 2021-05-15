# Django
from django.db import models


class Contact(models.Model):

    picture = models.ImageField(upload_to='contacts/picture')

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)

    occupation = models.CharField(max_length=30)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname
