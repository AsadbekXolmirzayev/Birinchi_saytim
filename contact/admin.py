from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "phone", "created_date"]
    date_hierarchy = 'created_date'
    search_fields = ["name", "email", "phone"]


admin.site.register(Contact, ContactAdmin)
