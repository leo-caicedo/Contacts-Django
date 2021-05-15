# Django
from django.urls import path

# Views
from app_contacts import views


app_name = 'app_contacts'
urlpatterns = [
    path('', views.main, name='main')
]
