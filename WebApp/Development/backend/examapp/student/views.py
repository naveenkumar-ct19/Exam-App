from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from general.decorators import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_user=['students'])
def courses(request):
    return render(request, 'student/courses.html')


@login_required(login_url='login')
@allowed_users(allowed_user=['students'])
def profile(request):
    return render(request, 'student/profile.html')


@login_required(login_url='login')
@allowed_users(allowed_user=['students'])
def index(request):
    return redirect('studentCourses')
