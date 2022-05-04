from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth import get_user_model
import hashlib
from django.contrib.auth.models import Group


class AccountManager(UserManager):

    def create_user(self, email, password, first_name=None, last_name=None, reg_id=None, dept_name=None, is_admin=False, is_staff=False, is_student=False, is_institution=False):
        if not email:
            raise ValueError("Users must have email address!")
        if not password:
            raise ValueError("Accounts must have password!")
        username = hashlib.md5(email.encode()).hexdigest()
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.is_admin = is_admin
        user.is_staff = is_staff
        user.is_active = True
        user.reg_id = reg_id
        user.dept_name = dept_name
        user.first_name = first_name
        user.last_name = last_name
        user.is_student = is_student
        user.is_institution = is_institution
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, first_name=None, last_name=None, reg_id=None, dept_name=None, is_admin=False, is_staff=False, is_student=False, is_institution=False):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name, last_name=last_name, reg_id=reg_id, dept_name=dept_name
        )
        user.is_admin = True
        user.is_staff = True
        user.is_student = True
        user.is_institution = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractUser):
    id = models.AutoField(
        auto_created=True, verbose_name="ID", primary_key=True)
    email = models.EmailField(
        verbose_name="Email Address", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='Date Joined', auto_now_add=True)
    last_login = models.DateTimeField(
        verbose_name='Last Login', auto_now=True)
    is_admin = models.BooleanField(verbose_name='Admin', default=False)
    is_institution = models.BooleanField(
        default=False, verbose_name='Institution')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    is_staff = models.BooleanField(default=False, verbose_name='Staff')
    is_student = models.BooleanField(default=False, verbose_name='Student')
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    reg_id = models.CharField(max_length=20, verbose_name='Reg ID')
    dept_name = models.CharField(max_length=50, verbose_name='Department')
    image_url = models.URLField(verbose_name="Profile Image")

    objects = AccountManager()

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'password',
                       'first_name', 'last_name', 'reg_id', 'dept_name', 'is_student', 'is_institution', 'is_staff']


class Course(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50)
    desc = models.TextField(verbose_name="Description")
    tutor = models.ForeignKey(
        Account, verbose_name="Tutor", on_delete=models.DO_NOTHING)


class Enrollments(models.Model):
    studentId = models.IntegerField(verbose_name="Student ID")
    tutorId = models.IntegerField(verbose_name="Tutor ID")
    courseId = models.IntegerField(verbose_name="Course ID")
