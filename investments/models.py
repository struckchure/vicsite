from django.db import models
from transactions.models import InvestmentStatus


class Package(models.Model):
    maximum_stake = models.DecimalField(max_digits=6, decimal_places=2)
    minimum_stake = models.DecimalField(max_digits=3, decimal_places=2)
    roi = models.PositiveIntegerField()
    duration = models.CharField(max_length=30)


class Investment(models.Model):
    sn = models.PositiveIntegerField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    status = models.ForeignKey(InvestmentStatus, on_delete=models.CASCADE, null=True)