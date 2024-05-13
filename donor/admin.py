from django.contrib import admin
from .models import Donor

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender', 'blood_type', 'organ_donated', ]
    search_fields = ['name', 'organ_donated', ]
    list_filter = ['gender', 'blood_type', 'organ_donated', ]
