from django.urls import path, include
from . import views

app_name = 'user'
urlpatterns = [
    path('reset/', include('django.contrib.auth.urls')),  # Include Django's built-in auth URLs for password reset
    path('signin/', views.signin_view, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('signup/success/', views.signup_success, name='signup_success'),
    path('profile/', views.view_profile, name='view_profile'),  # Add this line for the view_profile URL
]