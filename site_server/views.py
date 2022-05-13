from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.http import request
from accounts.models import Balance, DueDate, AmountInvested, CustomUser, Profilepic
from transactions.models import Deposit, Package
from contents.models import Carousel_Home, Carousel_About, Who_we_are, Who_we_are_sub, Top_executive, Top_executive_body, Our_offering, AboutUs, Footer, HowToInvest

class ChartView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("login")
    template_name = "charts.html"

    

class DashboardHomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("login")
    template_name = "home/home.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "wallet_bal": Balance.objects.filter(user=self.request.user).first(),
            "amount_invested": AmountInvested.objects.filter(user=self.request.user).first(),
            "duedate": DueDate.objects.filter(user=self.request.user).first(),
            "deposit_h": Deposit.objects.filter(user=self.request.user),
            "pics": Profilepic.objects.filter(user=self.request.user)
        }
        return context

class HomePageView(TemplateView):
    template_name = "front/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["carousel_home"] = Carousel_Home.objects.all()
        context = {
            "package": Package.objects.all(),
            "HTI": HowToInvest.objects.all(),
            "aboutus": AboutUs.objects.all(),
            "our_offering": Our_offering.objects.all(),
            "who_we_are": Who_we_are(),
            "carousel_home": Carousel_Home.objects.all(),
        }
        return context

class AboutPage(FormView):
    template_name = "front/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["carousel_home"] = Carousel_Home.objects.all()
        context = {
            "package": Package.objects.all(),
            "HTI": HowToInvest.objects.all(),
            "aboutus": AboutUs.objects.all(),
            "our_offering": Our_offering.objects.all(),
            "who_we_are": Who_we_are(),
            "carousel_home": Carousel_Home.objects.all(),
        }
        return context
    
 
class Custom_PasswordResetView(PasswordResetView):
    template_name = "password/forgot_password.html"
    subject_template_name = 'password/password_reset_subject.html'
    email_template_name = 'password/password_reset_email.html'
    success_url = reverse_lazy("c_password_reset_done")

class Custom_PasswordResetDoneView(PasswordResetDoneView):
    template_name = "password/password_reset_done.html"
    success_url = reverse_lazy("c_password_reset_confirm")

class Custom_PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "password/password_reset_confirm.html"
    success_url = reverse_lazy("c_password_reset_complete")

class Custom_PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "password/password_reset_complete.html"