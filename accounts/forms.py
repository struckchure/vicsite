from django import forms
from django.forms import ModelForm 
from django.db import models, transaction
from django.forms import ModelChoiceField
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from allauth.account.forms import LoginForm, SignupForm
from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            "firstname",
            "lastname",
            "occupation",
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
        self.fields['phone'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Enter your phone number here'})
        self.fields['sex'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
        self.fields['email'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Please enter a valid email address'})
        self.fields['password1'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
        self.fields['password2'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            "firstname",
            "lastname",
            "occupation",
            "email",
            "phone",
            "sex",
        )

class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Enter your email address here', 'name': 'login'})
        self.fields['password'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})

class CustomSignupForm(SignupForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    occupation = forms.ChoiceField(choices=[("Student", "Student"), ("Employed", "Employed"), ("Unemployed", "Unemployed"),("Self-Employed", "Self-Employed"), ("Others", "Others"),])
    sex = forms.ChoiceField(choices=[("Male", "Male"), ("Female", "Female")])
    phone = forms.CharField()
    email = forms.EmailField()
    password = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = CustomUser
        fields = ("firstname", "lastname", "occupation", "sex", "phone", "email", "password1", "password2")


    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)

        self.fields['firstname'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Enter your Firstname here'})
        self.fields['lastname'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Enter your Last name here'})
        self.fields['occupation'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
        self.fields['sex'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
        self.fields['phone'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Enter your phone number here'})
        self.fields['sex'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
        self.fields['email'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Please enter a valid email address'})
        self.fields['password1'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
        self.fields['password2'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)

        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        user.occupation = self.cleaned_data['occupation']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.sex = self.cleaned_data['sex']
        user.save()
        return user

    # Link to code snipppet
    # https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/

# class CustomSignupForm(SignupForm):

#     def __init__(self, *args, **kwargs):
#         super(CustomSignupForm, self).__init__(*args, **kwargs)

#         self.fields['firstname'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Enter your Firstname here'})
#         self.fields['lastname'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Enter your Last name here'})
#         self.fields['occupation'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
#         self.fields['sex'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
#         self.fields['phone'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Enter your phone number here'})
#         self.fields['sex'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
#         self.fields['email'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30', 'placeholder': 'Please enter a valid email address'})
#         self.fields['password1'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})
#         self.fields['password2'].widget.attrs.update({'class': 'block w-full border border-gray-200 rounded-md py-2 px-4 mt-2 focus:border-blue-400 focus:ring-blue-300 focus:ring focus:outline-none focus:ring-opacity-30'})

#     class Meta:
#         model = CustomUser
#         fields = ("firstname", "lastname", "occupation", "sex", "phone", "email", "password1", "password2")


