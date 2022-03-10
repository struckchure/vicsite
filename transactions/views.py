from rest_framework import generics
from transactions.models import Deposit, Withdraw
from transactions.serializers import DepositHistorySerializer, WithdrawSerializer, DepositFormSerializer

class DepositView(generics.CreateAPIView):
    '''
    This class handles the deposit request form
    '''
    queryset = Deposit.objects.all()
    serializer_class = DepositFormSerializer

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