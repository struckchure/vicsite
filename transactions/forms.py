from django import forms
from django.http import request
from transactions.models import Withdraw, Deposit

class WithdrawForm(forms.ModelForm):

    class Meta:
        model = Withdraw
        fields = ("coin", "wallet_address", "amount",) 

    def __init__(self, *args, **kwargs):
        super(WithdrawForm, self).__init__(*args, **kwargs)

        self.fields["coin"].widget.attrs.update({"class": "block w-full border border-blue-400 py-4 px-4 mt-3 focus:border-blue-500 focus:ring-blue300 focus:ring focus:outline-none focus:ring-opacity-30"})
        self.fields["wallet_address"].widget.attrs.update({"class": "block w-full border border-blue-400 py-4 mt-3 px-4 focus:border-blue-500 focus:ring-blue300 focus:ring focus:outline-none focus:ring-opacity-30"})
        self.fields["amount"].widget.attrs.update({"class": "block w-full border border-blue-400 py-4 mt-3 px-4 focus:border-blue-500 focus:ring-blue300 focus:ring focus:outline-none focus:ring-opacity-30", "placeholder": "$1000"})
        # self.fields["balance"].widget.attrs.update({"class": "block w-full py-4 mt-3 px-4 bg-gray-300"})

    def save(self, request):
        self.instance.user = request.user
        self.coin = self.cleaned_data['coin']
        self.wallet_address = self.cleaned_data['wallet_address']
        self.amount = self.cleaned_data['amount']
        super(WithdrawForm, self).save(request)


class DepositForm(forms.ModelForm):

    class Meta:
        model = Deposit
        fields = ("coin", "package", "company_wallet_address", "amount", "proof")

    def __init__(self, *args, **kwargs):
        super(DepositForm, self).__init__(*args, **kwargs)

        self.fields["package"].widget.attrs.update({"class": "block w-full border border-blue-400 py-4 px-4 mt-3 focus:border-blue-500 focus:ring-blue300 focus:ring focus:outline-none focus:ring-opacity-30"})
        self.fields["coin"].widget.attrs.update({"class": "block w-full border border-blue-400 py-4 px-4 mt-3 focus:border-blue-500 focus:ring-blue300 focus:ring focus:outline-none focus:ring-opacity-30"})
        self.fields["company_wallet_address"].widget.attrs.update({"class": "block w-full border border-blue-400 py-4 mt-3 px-4 focus:border-blue-500 focus:ring-blue300 focus:ring focus:outline-none focus:ring-opacity-30"})
        self.fields["amount"].widget.attrs.update({"class": "block w-full border border-blue-400 py-4 mt-3 px-4 focus:border-blue-500 focus:ring-blue300 focus:ring focus:outline-none focus:ring-opacity-30", "placeholder": "$1000"})
        self.fields["proof"].widget.attrs.update({"class": "block bg-white w-full border border-blue-400 py-4 mt-3 px-4 focus:border-blue-500 focus:ring-blue300 focus:ring focus:outline-none focus:ring-opacity-30"})

    def save(self, request):
        self.instance.user = request.user
        self.coin = self.cleaned_data['coin']
        self.package = self.cleaned_data['package']
        self.company_wallet_address = self.cleaned_data['company_wallet_address']
        self.amount = self.cleaned_data['amount']
        self.proof = self.cleaned_data['proof']
        super(DepositForm, self).save(request)
