# Generated by Django 4.0.3 on 2022-03-09 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CoinAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_wallet_address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_address', models.CharField(max_length=500)),
                ('balance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccounts.balance')),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccounts.coinaddress')),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('proof', models.ImageField(upload_to='')),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccounts.coin')),
                ('company_wallet_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccounts.coinaddress')),
            ],
        ),
    ]
