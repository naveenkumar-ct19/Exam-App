from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

handler404 = 'general.views.errorPage'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('tutor/', include('tutor.urls')),
    path('', include('general.urls')),
]


# "D:\ExamApp\WebApp\Development\backend\env\Scripts\python.exe" manage.py runserver
