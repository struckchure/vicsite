from django import forms
from django.forms import ModelForm 
from django.db import models, transaction
from django.forms import ModelChoiceField
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "occupation",
            "phone",
            "sex",
        )
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['firstname'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Enter your Firstname here'})
        self.fields['lastname'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Enter your Last name here'})
        self.fields['occupation'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
        self.fields['sex'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
        self.fields['phone'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Enter your phone number here'})
        self.fields['sex'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
        self.fields['email'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Please enter a valid email address'})
        self.fields['password1'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
        self.fields['password2'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class CustomSignupForm(CustomUserCreationForm):

    class Meta:
        model = CustomUser
        fields = CustomUserCreationForm.Meta.fields + (
            'sex',
            'occupation',
            'phone',
        )