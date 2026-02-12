from django.shortcuts import render,redirect
from base.models import Shedule
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='base:login')
def homepage(request):
    contex = {}
    if request.user.is_superuser == 1:
        contex['schedules'] = Shedule.objects.filter().order_by('-priority').order_by('-created_at')
    else:
        contex['schedules'] = Shedule.objects.filter(user=request.user).order_by('-priority').order_by('-created_at')
    return render(request,'base/index.html',contex)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('base:homepage')
    
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        passwd = request.POST.get('password').strip()

        if username is None or passwd is None:
            messages.error(request,'User Name or Password cant be empty')

        user = User.objects.filter(username=username).first()
        if user:
            user = authenticate(request,username=username,password=passwd)

        if user:
            login(request,user)
            request.session.set_expiry(0)
            return redirect('base:homepage')
        
        messages.error(request,'User Name or Password is invalide')
        return render(request,'base/login.html')

    return render(request,'base/login.html')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('base:homepage')
    
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        passwd = request.POST.get('password1').strip()
        email = request.POST.get('email').strip()
        
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request,'invalid email')
        
        if username is None or passwd is None:
            messages.error(request,'User Name or Password cant be empty')
        
        elif len(passwd)<5:
            messages.error(request,'minimum password length is 5 charaters')
        
        elif User.objects.filter(Q(username=username) | Q(email=email)).exists():
            messages.error(request,'username or email already taken')

        else:
            user = User.objects.create_user(username=username,email=email,password=passwd)
            user.save() 
            messages.success(request, "User created successfully!") 
            return redirect("base:login")
        
    return render(request,'base/register.html')

def logout_user(request):
    if request.user and request.user.is_authenticated:
        logout(request)
    
    return redirect('base:login')