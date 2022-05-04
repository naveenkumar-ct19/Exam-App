from django import forms
from django.forms import ValidationError
from general.models import Course


class AddCourseForm(forms.ModelForm):

    title = forms.CharField(max_length=50, required=True)
    desc = forms.CharField(max_length=200, required=True)

    class Meta:
        model = Course
        fields = ('title', 'desc',)
        exclude = ["tutor"]

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def clean_title(self):
        data = self.cleaned_data.get("title")
        if len(data) < 5:
            raise ValidationError("No title")
        return data

    def clean_description(self):
        data = self.cleaned_data.get("desc")
        if len(data) < 5:
            raise ValidationError("No description")
        return data
