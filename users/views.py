from rest_framework import generics
from users.models import Deposit, Withdraw, Balance, UserCryptoDetails
from users.serializers import UserBalanceSerializer, UserCryptoDetails

# Create your views here.
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