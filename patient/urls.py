from django.urls import path
from . import views

# from django.contrib.auth import views as auth_views

app_name="patient"
urlpatterns = [
    path('', views.patientLandingPage, name='patient_landingPage'),
    path('search/', views.search_donors, name='search_donors'),
    path('list/', views.search_patient, name='search_results'),
]

