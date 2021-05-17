# Django
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

# Models
from app_contacts.models import Contact

# Forms
from app_contacts.forms import ContactForm


class Home(ListView):

    template_name = 'contacts/home.html'
    model = Contact
    context_object_name = 'contacts'


class ContactCreate(CreateView):

    template_name = 'contacts/new.html'
    form_class = ContactForm
    success_url = reverse_lazy('contacts:home')


class ContactUpdate(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/new.html'
    success_url = reverse_lazy('contacts:home')


class ContactDelete(DeleteView):
    model = Contact
    template_name = 'contacts/delete.html'
    success_url = reverse_lazy('contacts:home')
