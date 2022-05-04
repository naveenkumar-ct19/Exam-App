from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from .models import Account as User
from .decorators import allowed_users


def login(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            email = loginForm.cleaned_data.get('email')
            password = loginForm.cleaned_data.get('password')
            try:
                user = User.objects.get(email=email)
                user = authenticate(username=user.email, password=password)
                if user != None:
                    authLogin(request, user)
                    messages.add_message(
                        request, messages.SUCCESS, 'Login Successful!')
                    return redirect(request.GET.get('next', 'home'))
                else:
                    messages.add_message(
                        request, messages.INFO, 'Invalid Email / Password!')
                    return redirect('login')
            except User.DoesNotExist:
                messages.add_message(
                    request, messages.INFO, "I think you don't have an account!")
                return redirect('login')
        else:
            messages.add_message(
                request, messages.INFO, 'Nice try! Mr. Hacker!')
            return redirect('login')
    else:
        return render(request, 'general/login.html')


@login_required(login_url='login')
@allowed_users(allowed_user=['institution'])
def register(request):
    if request.method == 'POST':
        print(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            dept = form.cleaned_data.get('dept')
            firstName = form.cleaned_data.get('first_name')
            lastName = form.cleaned_data.get('last_name')
            role = form.cleaned_data.get('role')
            regID = form.cleaned_data.get('regID')
            print(
                email and password and dept and role and regID and firstName and lastName)
            user = User.objects.create_user(email=email, password=password, first_name=firstName, last_name=lastName, reg_id=regID,
                                            dept_name=dept, is_admin=False, is_staff=(role == 'tutor'), is_student=(role == 'student'), is_institution=False)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Account Created!')
            return redirect('register')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error in  creating the account!')
            return redirect('register')
    else:
        return render(request, 'general/register.html')


@login_required(login_url='login')
def logout(request):
    authLogout(request)
    messages.add_message(request, messages.SUCCESS, 'Logout Successful!')
    return redirect('login')


def help(request):
    return render(request, 'general/help.html')


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.user.is_student:
            return redirect('student')
        elif request.user.is_staff:
            return redirect('tutor')
        elif request.user.is_institution:
            return redirect('register')


def errorPage(request, exception):
    return render(request, 'error.html')
