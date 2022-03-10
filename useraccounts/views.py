from rest_framework import generics
from useraccounts.models import Deposit, Withdraw, Balance, UserCryptoDetails
from useraccounts.serializers import DepositHistorySerializer, WithdrawSerializer, DepositFormSerializer, UserBalanceSerializer, UserCryptoDetails


class DepositHistoryView(generics.ListAPIView):
    '''
    This class displays the deposit history for a user
    '''
    queryset = Deposit.objects.all()
    serializer_class = DepositHistorySerializer

class WithdrawView(generics.CreateAPIView):
    '''
    This class handles the form for withdraw request
    '''
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer

class WithdrawHistory(generics.ListAPIView):
    ''' 
    This class handles the response for viewing withdraw history
    '''
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer


class DepositView(generics.CreateAPIView):
    '''
    This class handles the deposit request form
    '''
    queryset = Deposit.objects.all()
    serializer_class = DepositFormSerializer

class UserBalanceView(generics.RetrieveAPIView):
    '''
    Returns User Balance
    '''
    queryset = Balance.objects.all()
    serializer_class = UserBalanceSerializer

class UserAssetView(generics.ListCreateAPIView):
    '''
    Returns User Asset Details. Edit List
    '''
    queryset = UserCryptoDetails
    serializer_class = UserCryptoDetails