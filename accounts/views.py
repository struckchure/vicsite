from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import request, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from accounts.models import Contact
from accounts.forms import CustomLoginForm, CustomSignupForm


# Create your views here.
class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("home")

def SignupView(request):
    if request.method == "POST":
        form = CustomSignupForm(request.POST)

        if form.is_valid():
            form.save(request)
            # print("form is saved")

            return HttpResponseRedirect(reverse_lazy("login"))
            # return reverse_lazy("login")
            # return HttpResponse("It is saved")
    else:
        # print("Form is not saved")
        form = CustomSignupForm()
    return render(request, "registration/register.html", {"form": form})

class ContactView(CreateView):
    ''' Contact us Form '''
    model = Contact
    fields = "__all__"
