from django.urls import path
from . import views

app_name="donor"
urlpatterns = [
    path('', views.donorLandingPage, name='donor_landingPage'),
    path('register/', views.donorRegisteration, name='donor_registration'),
    path('login/', views.donorLogin, name='donor_login'),
    path('donate/', views.donate, name='donate'),
]
