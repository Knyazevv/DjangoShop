from django.contrib import admin

from product.models import ContactFormEntry


class ContactFormEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message')
    list_display_links = ('id', 'name')


admin.site.register(ContactFormEntry, ContactFormEntryAdmin)