from django.shortcuts import render, redirect
from .forms import TeacherRegisterForm, StudentRegisterForm, UserTypeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from . import reg_email

def register_user_type(request):
    if request.method == 'POST':
        form = UserTypeForm(request.POST)
        if form.is_valid():
            user_type = form.cleaned_data['user_type']
            if user_type == 'teacher':
                return redirect('register_teacher')
            elif user_type == 'student':
                return redirect('register_student')
    else:
        form = UserTypeForm()
    return render(request, 'users/register_user_type.html', {'form': form})


def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            reg_email.registration_email(user)
            return redirect('registration_success')
    else:
        form = TeacherRegisterForm()
    return render(request, 'users/register_teacher.html', {'form': form})


def register_student(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            reg_email.registration_email(user)
            return redirect('registration_success')
    else:
        form = StudentRegisterForm()
    return render(request, 'users/register_student.html', {'form': form})


def registration_success(request):
    return render(request, 'users/registration_success.html')


def login_view(request):
    form = AuthenticationForm(request.POST)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

def profile_view(request):
    user = request.user
    return render(request, 'users/profile.html', {'user':user})