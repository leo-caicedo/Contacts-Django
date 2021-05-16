# Django
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

# Models
from app_contacts.models import Contact

# Forms
from app_contacts.forms import ContactForm


class ContactList(ListView):

    template_name = 'app_contacts/base.html'
    model = Contact
    context_object_name = 'contacts'


class ContactCreate(CreateView):

    template_name = 'app_contacts/new.html'
    form_class = ContactForm
    success_url = reverse_lazy('app_contacts:list')


class ContactUpdate(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'app_contacts/new.html'
    success_url = reverse_lazy('app_contacts:list')


class ContactDelete(DeleteView):
    model = Contact
    template_name = 'app_contacts/delete.html'
    success_url = reverse_lazy('app_contacts:list')
