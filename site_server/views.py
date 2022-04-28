from django.views.generic import TemplateView
from accounts.models import Balance, DueDate, AmountInvested

class ChartView(TemplateView):
    template_name = "charts.html"


class DashboardHomeView(TemplateView):
    template_name = "home/home.html"

    extra_context = {
        "wallet_bal": Balance.objects.all(),
        "amount_invested": AmountInvested.objects.all(),
        "duedate": DueDate.objects.all(),
    }