from django import forms

from .models import Product



class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "The Title is: "}))
    email= forms.EmailField(required=False, widget=forms.TextInput(attrs={"placeholder": "The Email is: "}))
    description = forms.CharField(required=False, widget=forms.Textarea(

        attrs={"class": "form-control",
               "placeholder": "The Description is: ",
               'rows': 15,
               'cols': 50,
               "id": "my-id-for-textarea",
               }))
    price = forms.DecimalField(required=False, initial=0.00)
    summary = forms.CharField(required=False, widget=forms.Textarea(attrs={

        "placeholder": "The Summary is: ",
        'rows': 15,
        'cols': 52
    }))
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'summary']

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get('title')
    #     if not "new" in title:
    #         raise forms.ValidationError("Title is not valid")
    #     return title
    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     if not "@" in email:
    #         raise forms.ValidationError("Email is not valid")
    #     return email



class RawProductForm(forms.Form):
    title = forms.CharField(label= '', widget= forms.TextInput(attrs={"placeholder":"The Title is: "}))
    description = forms.CharField(required=False, widget=forms.Textarea(

        attrs={"class": "form-control",
               "placeholder":"The Description is: ",
               'rows': 15,
               'cols': 50,
               "id": "my-id-for-textarea",
            }))
    price = forms.DecimalField(initial = 0.00)
    summary = forms.CharField(widget=forms.Textarea(attrs={

        "placeholder":"The Summary is: ",
        'rows': 15,
        'cols': 52
    }))




