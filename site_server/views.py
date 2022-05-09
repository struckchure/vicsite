from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
# from django.http import request
from accounts.models import Balance, DueDate, AmountInvested, CustomUser

class ChartView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("login")
    template_name = "charts.html"

    

class DashboardHomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("login")
    template_name = "home/home.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "wallet_bal": Balance.objects.filter(user=self.request.user),
            "amount_invested": AmountInvested.objects.filter(user=self.request.user),
            "duedate": DueDate.objects.filter(user=self.request.user),
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