# Django
from django.contrib import admin

# Models
from app_contacts.models import Contact


#@admin.register(Contact)
#class ContactsAdmin(admin.ModelAdmin):
#
#    list_display = ('pk', 'firstname', 'lastname', 'phone', 'email', 'occupation', 'picture')
#    list_display_links = ('pk', 'firstname')
#    list_editable = ('phone', 'picture')
#
#    search_fields = ('firstname', 'lastname', 'phone', 'phone', 'email', 'occupation')
#
#    list_filter = ('created', 'modified')
#
#    readonly_fields = ('created', 'modified')


admin.site.register(Contact)
