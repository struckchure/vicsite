from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from investments.models import Investment, Package
from accounts.models import CustomUser


class InvestView(LoginRequiredMixin, ListView):
    """
    This class displays the investment form
    """
    login_url = reverse_lazy("login")
    model = Investment
    template_name = "investments/invest.html"
    # success_url = reverse_lazy("dashboard")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "user": self.request.user,
            "package": Package.objects.all(),
        }
        return context
    

