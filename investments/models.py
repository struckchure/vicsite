from django.db import models
from transactions.models import InvestmentStatus
from useraccounts.models import Balance


class Package(models.Model):
    maximum_stake = models.DecimalField(max_digits=6, decimal_places=2)
    minimum_stake = models.DecimalField(max_digits=3, decimal_places=2)
    roi = models.PositiveIntegerField()
    duration = models.CharField(max_length=30)


class Investment(models.Model):
    sn = models.PositiveIntegerField()
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE, null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    status = models.ForeignKey(InvestmentStatus, on_delete=models.CASCADE, null=True)