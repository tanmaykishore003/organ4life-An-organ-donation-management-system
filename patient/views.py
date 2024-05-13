from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from donor.models import Donor


# Create your views here.


def patientLandingPage(request):
    return render(request, 'patient/patient_landingPage.html')

@login_required
def search_donors(request):

    if request.method == 'GET':
        blood = request.GET.get('blood_type')
        organ = request.GET.get('organ_needed')

        if blood == 'Any' and organ == 'Any':
            matching_donors = Donor.objects.all()
        else:
            matching_donors = Donor.objects.filter(blood_type=blood, organ_donated=organ)

        return render(request, 'patient/search_form.html', {'donors': matching_donors})

    elif request.method == 'POST':
        
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        blood_type = request.POST.get('blood_type')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        email = request.POST.get('email')
        medical_condition = request.POST.get('medical_condition')
        urgency_level = request.POST.get('urgency_level')
        donor_name = request.POST.get('donor_name')
        hospital = request.POST.get('hospital_name')
        organ_needed = request.POST.get('organ_donated')
        

        patient = Patient.objects.create(
            name=name,
            age=age,
            gender=gender,
            blood_type=blood_type,
            phone_number=phone_number,
            email=email,
            address=address,
            medical_condition=medical_condition,
            urgency_level=urgency_level,
            donor_name=donor_name,
            hospital=hospital,
            organ_needed=organ_needed
        )

        patient.save()


        messages.success(request, "PATIENT ADDED SUCCESSFULLY")
        return redirect('/patient/search/')
        
    else:
        return render(request, 'patient/search_form.html')

@login_required
def search_patient(request):
    matching_patients = Patient.objects.all()
    return render(request, 'patient/search_results.html', {'matching_patients': matching_patients})
