from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def Signup(request):
    user_type=request.POST.get("user_type")
    first_name=request.POST.get("first_name")
    last_name=request.POST.get("last_name")
    profile_picture=request.FILES.get("profile_picture")
    user_name=request.POST.get("user_name")
    email_id=request.POST.get("email_id")
    password=request.POST.get("password")
    re_password=request.POST.get("re_password")
    address=request.POST.get("address")
    check_email=SignUp.objects.filter(User_Name=user_name)
    if request.method == 'POST':
        if (check_email):
            messages.error(request, "UserName Already registered. pls choose different username")
        else:
            if (password == re_password):
                save_details=SignUp(User_Type=user_type, First_Name=first_name, Last_Name=last_name,Profile_Picture=profile_picture, User_Name=user_name, Email_Id=email_id, Password=password, Address=address)
                save_details.save()
                user=User.objects.create_user(user_name, email_id, password)
                user.save()
                messages.success(request, "signup successfull")
                return redirect("Login")
            else:
                messages.warning(request, "Re-password didn't match with password")
    return render(request, "signup.html", locals())

def Login(request):
    if request.method == 'POST':
        user_name=request.POST.get("user_name")
        passwordd=request.POST.get("passwordd")
        user=authenticate(request, username=user_name, password=passwordd)
        get_data=SignUp.objects.filter(User_Name=user)
        for i in get_data:
            user_type=i.User_Type
        if user!=None:
            login(request, user)
            print(user)
            print(user_type)
            if user_type=='doctor':
                return redirect("Doctor")
            elif user_type=='patient':
                return redirect("Patient")
            else:
                messages.error(request, "user not fount")
        else:
            messages.error(request, "pls enter valid username and password")
    return render(request, "login.html", locals())

@login_required(login_url='Login')
def Doctor(request):
    details=SignUp.objects.get(User_Name=request.user)
    return render(request, "doctor_home.html", locals())

@login_required(login_url='Login')
def Patient(request):
    details=SignUp.objects.get(User_Name=request.user)
    return render(request, "patient_home.html", locals())

