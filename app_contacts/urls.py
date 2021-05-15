# Django
from django.urls import path

# Views
from app_contacts import views


app_name = 'app_contacts'
urlpatterns = [
    path('', views.ListContacts, name='list'),
    path('new', views.CreateContact, name='new')
]
