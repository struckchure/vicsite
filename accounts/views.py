from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from allauth.account.views import SignupView, LoginView
from accounts.models import Contact
from accounts.forms import CustomUserCreationForm, CustomLoginForm, CustomSignupForm


# Create your views here.
# class CustomLoginView(LoginView):
#     form_class = CustomLoginForm
#     success_url = reverse_lazy("home")
#     template_name = "registration/login.html"

# class CustomSignupView(SignupView):
#     form_class = CustomSignupForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/register.html"

class ContactView(CreateView):
    ''' Contact us Form '''
    model = Contact
    fields = "__all__"
