from email import message
from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpFrom
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'home.html')


@login_required
def login_home(request):
    return render(request, 'main.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpFrom()
    return render(request, 'registration/signup.html', {'form': form})


def TermsAndCondition(request):
    return render(request, 'termsAndCondition.html')


def password_change(request):
    return render(request, 'password_change_form.html')


def aboutUs(request):
    return render(request, 'aboutUs.html')


def ContactUs(request):
    return render(request, 'ContactUs.html')


def User_input(request):
    return render(request, 'User_input.html')