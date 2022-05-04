from django import forms
from django.forms import ValidationError


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=40)

    class Meta:
        fields = ('email', 'password')

    def clean_email(self):
        data = self.cleaned_data.get("email")
        return data

    def clean_password(self):
        data = self.cleaned_data.get("password")
        return data


class RegisterForm(forms.Form):
    ROLES = [('student', 'student'), ('tutor', 'tutor')]
    email = forms.EmailField()
    first_name = forms.CharField(max_length=40,)
    last_name = forms.CharField(max_length=40,)
    password = forms.CharField(max_length=40,)
    confirmPassword = forms.CharField(max_length=40,)
    role = forms.ChoiceField(choices=ROLES)
    regID = forms.CharField(max_length=30,)
    dept = forms.CharField(max_length=50,)

    class Meta:
        fields = ('email', 'first_name', 'last_name', 'password', 'confirmPassword',
                  'role', 'regID', 'dept')

    def clean_email(self):
        data = self.cleaned_data.get("email")
        if not data:
            raise ValidationError("No Email")
        return data

    def clean_password(self):
        data = self.cleaned_data.get("password")
        if not data:
            raise ValidationError("No Password")
        return data

    def clean_dept(self):
        data = self.cleaned_data.get("dept")
        if not data:
            raise ValidationError("No dept")
        return data

    def clean_role(self):
        data = self.cleaned_data.get("role")
        if not data:
            raise ValidationError("No role")
        return data

    def clean_confirmPassword(self):
        data = self.cleaned_data.get("confirmPassword")
        if not data:
            raise ValidationError("No confirmPassword")
        return data

    def clean_first_name(self):
        data = self.cleaned_data.get("first_name")
        if not data:
            raise ValidationError("No first_name")
        return data

    def clean_last_name(self):
        data = self.cleaned_data.get("last_name")
        if not data:
            raise ValidationError("No last_name")
        return data

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmPassword = cleaned_data.get('confirmPassword')
        if password != confirmPassword:
            raise ValidationError("Pass not Equal!")
        return cleaned_data
