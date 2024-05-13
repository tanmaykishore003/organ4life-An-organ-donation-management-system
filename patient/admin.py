from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender', 'blood_type', 'organ_needed', 'urgency_level', 'date_added']
    search_fields = ['name', 'organ_needed', 'medical_condition']
    list_filter = ['gender', 'blood_type', 'urgency_level', 'date_added']
