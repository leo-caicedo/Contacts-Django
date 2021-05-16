# Django
from django.urls import path

# Views
from app_contacts import views


app_name = 'contacts'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('new', views.ContactCreate.as_view(), name='new'),
    path('delete/<int:pk>', views.ContactDelete.as_view(), name='delete'),
    path('update/<int:pk>', views.ContactUpdate.as_view(), name='update'),
]
