from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import Company_profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter First name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter last name'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter Email address'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter username'}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter Password'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'ReEnter Password'}), required=True)
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',] 
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email is already exists.')
    
class CompanyFORM(forms.ModelForm):
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Company Name'}), required=True)
    company_location = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Enter Company Location','rows': 4, 'cols': 40}), required=True)
    about_company = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Enter About Company','rows': 4, 'cols': 40}), required=True)
    website_url = forms.URLField(widget=forms.URLInput(attrs={'class':'form-control', 'placeholder': 'Enter Company Website URL'}), required=False)
    founded_on = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control', 'placeholder': 'Select the company found date'}))
    company_size = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Enter the Company Size'}), required=True)
    specilities = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Company Specialities'}), required=True)
    active = forms.CheckboxInput(attrs={'class':'form-check-input'})
    
    class Meta:
        model = Company_profile
        fields = [
            'company_name','about_company','company_location','website_url','founded_on','company_size','specilities','active','group_name'
        ]