from rest_framework import generics, permissions
from accounts.models import Balance, UserCryptoDetails
from accounts.serializers import UserBalanceSerializer, UserCryptoDetails

# Create your views here.
class UserBalanceView(generics.RetrieveAPIView):
    '''
    Returns User Balance
    '''
    queryset = Balance.objects.all()
    serializer_class = UserBalanceSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserAssetView(generics.ListCreateAPIView):
    '''
    Returns User Asset Details. Edit List
    '''
    queryset = UserCryptoDetails
    serializer_class = UserCryptoDetails
    permission_classes = (permissions.IsAuthenticated,)