from django.urls import path
from . import views

app_name='hospital'
urlpatterns = [
    path('', views.landingPage, name='landing_page'),
    path('all_login', views.all_login, name='all_login'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('review/', views.reviews, name="reviews"),
    path('logout/', views.custom_logout, name="custom_logout"),

]

