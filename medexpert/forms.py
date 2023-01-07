from django import forms
from .models import Emergency
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Table(forms.ModelForm):
    class Meta:
        model = Emergency
        fields = '__all__'


class Reg(UserCreationForm):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    phonenumber = forms.CharField(widget=forms.NumberInput(attrs={'type': 'number', 'class': 'form-control'}))
    dateofbirth = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    gender = forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect())
    email = forms.CharField(widget=forms.EmailInput(attrs={'type': 'email', 'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email','phonenumber','gender', 'dateofbirth')
'''
pno
email
date of birth
gender
pass
fname
lname
'''
