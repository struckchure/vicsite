from django.contrib.auth.mixins import LoginRequiredMixin
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
    
    