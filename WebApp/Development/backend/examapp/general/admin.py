from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Course


class CoursesAdmin(admin.ModelAdmin):
    model = Course
    list_display = ['id', 'title', 'desc', 'tutor']


class AccountAdmin(UserAdmin):

    model = Account
    list_display = ['id', 'email', 'username', 'first_name',
                    'last_name', 'is_student', 'is_staff', 'is_institution']
    readonly_fields = ('date_joined', 'last_login')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {
         'fields': ('first_name', 'last_name', 'email', 'reg_id', 'dept_name')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_student', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'is_student', 'is_staff', 'reg_id', 'password1', 'password2'),
        }),
    )


admin.site.register(Account, AccountAdmin)
admin.site.register(Course, CoursesAdmin)
