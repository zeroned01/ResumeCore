from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home , name='home'),
    path('signup/', views.signup, name = 'signup'),
    path('terms/', views.TermsAndCondition, name= 'termsAndCondition'),
    path("About/", views.aboutUs, name="aboutUs"),
    path('change-password', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'), name='password_change'),
    path('main/', views.login_home, name='login_home'),
    path('contactUs/', views.ContactUs, name = 'ContactUs'),
    path('main/User_input/', views.User_input, name= 'User_input')
]
