# Django
from django.shortcuts import render


def main(request):
    return render(request, 'app_contacts/base.html', {'name': 'Leo'})
