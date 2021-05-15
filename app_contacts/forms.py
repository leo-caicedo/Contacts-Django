# Django
from django import forms

# Models
from app_contacts.models import Contact


class ContactForm(forms.ModelForm):
    """Contact model form"""

    class Meta:
        """Form settings"""

        model = Contact
        fields = ('picture', 'firstname', 'lastname', 'phone', 'email', 'occupation')
