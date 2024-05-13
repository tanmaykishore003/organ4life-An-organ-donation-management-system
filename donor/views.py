from django.shortcuts import render, redirect
from .models import Donor
from hospital.models import Hospital
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *



# Create your views here.


def donorLandingPage(request):
    return render(request, 'donor/donor_landingPage.html')


def donorRegisteration(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
         
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/donor/register/')
         
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
         
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
         
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/donor/register/')


    return render(request, 'donor/donor_registration.html')

def donorLogin(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/donor/login/')
         
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
         
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/donor/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/donor/donate/')
     
    
    return render(request, 'donor/donor_login.html')


@login_required
def donate(request):

    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        blood_type = request.POST.get('blood_type')
        organ_donated = request.POST.get('organ_donated')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        hospital = request.POST.get('hospital_name')
        profile_picture = request.FILES.get('profile_picture')
        print(hospital)

        # Create a new Donor instance with the provided data
        donor = Donor.objects.create(
            name=name,
            age=age,
            gender=gender,
            blood_type=blood_type,
            organ_donated=organ_donated,
            hospital=hospital,
            email=email,
            phone_number=phone_number,
            address=address,
            profile_picture=profile_picture
        )
        # Save the donor object
        donation = donor.save()

        # Redirect to a success page or do something else

        messages.success(request, "DONOR ADDED SUCCESSFULLY")
        return redirect('/donor/donate/')

    if not request.user.is_authenticated:
        return redirect('/login/')

    hospitals = Hospital.objects.all()
    return render(request, 'donor/donation_form.html', {'hospitals': hospitals})
