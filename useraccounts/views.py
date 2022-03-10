from rest_framework import generics
from useraccounts.models import Deposit, Withdraw, Balance, UserCryptoDetails
from useraccounts.serializers import UserBalanceSerializer, UserCryptoDetails




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