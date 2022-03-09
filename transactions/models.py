from django.conf import settings
from django.db import models

STATUS = (
    ('P', 'Pending'),
    ('F', 'Failed'),
    ('C', 'Completed'),
)

INVEST_STATUS = (
    ('A', 'Active'),
    ('N', 'Unactive'),
)

class TransactionHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sn = models.PositiveIntegerField()
    # deposit_
    

class DepositStatus(models.Model):
    deposit_status = models.CharField(max_length=20, choices=STATUS)


class WithdrawStatus(models.Model):
    withdraw_status = models.CharField(max_length=20, choices=STATUS)

class InvestmentStatus(models.Model):
    invest_status = models.CharField(max_length=20, choices=INVEST_STATUS, default=INVEST_STATUS[0][0])