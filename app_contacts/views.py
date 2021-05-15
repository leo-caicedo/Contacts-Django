# Django
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, ListView

# Models
from app_contacts.models import Contact

# Forms
from app_contacts.forms import ContactForm


class ListContacts(ListView):

    template_name = 'app_contacts/base.html'
    model = Contact
    context_object_name = 'contacts'


class CreateContact(CreateView):

    template_name = 'app_contacts/new.html'
    form_clas = ContactForm
    success_url = reverse_lazy('app_contacts/base')
