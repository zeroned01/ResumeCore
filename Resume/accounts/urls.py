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
    path('templets/', views.choose_templete, name='templets'),
    path('templetss/', views.choose_templete_aftervalue, name="templetss"),
    path('conform2/', views.conformForSecond, name="conformforS"),
    path('conform1/', views.conformForFirst, name="conformforF"),
    path('conform3/', views.conformForThird, name="conformforT"),
    path('eduform/', views.edu_form, name="edu"),
    path('work/', views.work_form, name="work"),
    path('awardsform/', views.awards_form, name="awards"),
    path('skillform/', views.skill_form, name="skill"),
    path('personalform/', views.personal_form, name="personal"),
    path('result1/', views.temp_Result1,name="result1"),
    path('result2/', views.temp_Result2,name="result2"),
    path('result3/', views.temp_Result3,name="result3")

]
