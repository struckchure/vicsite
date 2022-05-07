from django import forms
from django.forms import ModelForm 
from django.db import models, transaction
from django.forms import ModelChoiceField
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from accounts.models import CustomUser, Profilepic

OCCUPATION = (
    ("Student", "Student"),
    ("Employed", "Employed"),
    ("Unemployed", "Unemployed"),
    ("Self-Employed", "Self-Employed"),
    ("Others", "Others"),
)


SEX = (
    ("Male", "Male"),
    ("Female", "Female"),
)

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            "firstname",
            "lastname",
            "occupation",
            "phone",
            "email",
            "phone",
            "sex",
        )
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['firstname'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Enter your Firstname here'})
        self.fields['lastname'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Enter your Last name here'})
        self.fields['occupation'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
        self.fields['sex'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
        self.fields['phone'].widget.attrs.update({
            'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 
            'placeholder': 'Enter your phone number here',
            'type': 'tel',
            })
        self.fields['email'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Please enter a valid email address'})
        self.fields['password1'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
        self.fields['password2'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
    

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            "firstname",
            "lastname",
            "phone",
            "occupation",
            "email",
            "sex",
        )


class CustomSignupForm(CustomUserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            "firstname",
            "lastname",
            "occupation",
            "email",
            "phone",
            "sex",
            "password1",
            "password2",
        )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)

        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        user.occupation = self.cleaned_data['occupation']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.sex = self.cleaned_data['sex']

        # Password Validation
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password2 != password1:
            raise forms.ValidationError('Passwords don\'t match')
        else:
            return password2

        user.password = password2
        user.save()
        return user

class ProfilePicForm(ModelForm):
    class Meta:
        model = Profilepic
        fields = {"img",}

class CustomLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Enter your email address here', 'name': 'login'})
        self.fields['password'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})