from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from general.decorators import allowed_users
from .forms import AddCourseForm
from django.contrib import messages
from general.models import Course


@login_required(login_url='login')
@allowed_users(allowed_user=['teachers'])
def manageCourses(request, *args, **kwargs):
    course_id = kwargs.get('courseID')
    if course_id:
        courses = Course.objects.all().filter(
            tutor=request.user).filter(id=course_id)
        data = {'courses': courses}
        return render(request, 'tutor/courses.html', context=data)
    else:
        return redirect('tutorCourses')


@login_required(login_url='login')
@allowed_users(allowed_user=['teachers'])
def courses(request, *args, **kwargs):
    print(kwargs)
    courses = Course.objects.all().filter(tutor=request.user)
    data = {'courses': courses}
    return render(request, 'tutor/courses.html', context=data)


@login_required(login_url='login')
@allowed_users(allowed_user=['teachers'])
def profile(request):
    return render(request, 'tutor/profile.html')


@login_required(login_url='login')
@allowed_users(allowed_user=['teachers'])
def addCourse(request):
    if request.method == 'POST':
        tutor_id = {'tutor': int(request.user.id)}
        data = {'title': request.POST.get(
            'title'), 'desc': request.POST.get('description')}
        data.update(tutor_id)
        print(data)
        form = AddCourseForm(data)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('desc')
            print(title, description)
            course = form.save(commit=False)
            course.tutor = request.user
            course.save()
        else:
            print("Form is not valid!")
    return redirect('tutorCourses')


@login_required(login_url='login')
@allowed_users(allowed_user=['teachers'])
def index(request):
    return redirect('tutorCourses')
