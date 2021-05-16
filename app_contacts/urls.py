# Django
from django.urls import path

# Views
from app_contacts import views


app_name = 'app_contacts'
urlpatterns = [
    path('', views.ContactList.as_view(), name='list'),
    path('new', views.ContactCreate.as_view(), name='new'),
    path('delet/<int:pk>', views.ContactDelete.as_view(), name='delete'),
    path('update/<int:pk>', views.ContactUpdate.as_view(), name='update'),
]
