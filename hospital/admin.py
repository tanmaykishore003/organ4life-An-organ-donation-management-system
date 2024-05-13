from django.contrib import admin
from .models import Hospital

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact_number')
    search_fields = ('name', 'location')

admin.site.register(Hospital, HospitalAdmin)
