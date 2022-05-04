from django.contrib import admin
from django.urls import path, include
from student import views


urlpatterns = [
    path('', views.index, name='student'),
    path('courses', views.courses, name='studentCourses'),
    path('profile', views.profile, name='studentProfile'),
]
