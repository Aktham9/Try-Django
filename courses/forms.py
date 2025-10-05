from django import forms

from .models import Course

class CourseModelForm(forms.ModelForm):
    title= forms.CharField( widget=forms.TextInput(attrs={"placeholder": "The Title is: "}))
    class Meta:
        model = Course
        fields = ['title']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if title.lower() =='abc':
            raise forms.ValidationError('Title should not be "abc"')
        return title


