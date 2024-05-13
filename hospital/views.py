from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.

def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/patient/login/')
         
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
         
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            next_url = request.GET.get('next', '/')
            return redirect(next_url)

    return render(request, 'hospital/login.html')

def registerPage(request):
    
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
            return redirect('/register/')
         
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
        return redirect('/register/')

    return render(request, 'hospital/register.html')

def custom_logout(request):
    logout(request)
    return redirect('/') 

def landingPage(request):
    return render(request, 'hospital/landing_page.html')

def all_login(request):
    return render(request, 'hospital/all_login.html')

@login_required
def reviews(request):
    return render(request, 'hospital/reviews.html')

def custom_404_view(request, exception):
    print("Custom 404 handler called!")
    # Render a custom HTML template for the 404 page
    return render(request, 'hospital/errorPage.html', status=404)