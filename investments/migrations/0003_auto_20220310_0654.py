# Generated by Django 3.2.11 on 2022-03-10 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0004_withdraw_amount'),
        ('investments', '0002_investment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='balance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='useraccounts.balance'),
        ),
    ]