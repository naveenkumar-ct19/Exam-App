from django.contrib import admin
from django.urls import path, include
from tutor import views


urlpatterns = [
    path('', views.index, name='tutor'),
    path('courses', views.courses, name='tutorCourses'),
    path('courses/add/', views.addCourse, name='addCourses'),
    path('courses/manage/<int:courseID>',
         views.manageCourses, name='manageCourses'),
    path('profile', views.profile, name='tutorProfile'),
]
