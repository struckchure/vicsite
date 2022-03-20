from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.models import Balance, UserCryptoDetails
from accounts.serializers import UserBalanceSerializer, UserCryptoDetails

# Create your views here.
class UserBalanceView(generics.RetrieveAPIView):
    """
    Returns User Balance
    """

    serializer_class = UserBalanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This should return balance of the authenticated user
        """
        user = self.request.user
        bal = Balance.objects.filter(user=user)
        return bal


class UserAssetView(generics.ListCreateAPIView):
    """
    Returns User Asset Details. Edit List
    """

    queryset = UserCryptoDetails
    serializer_class = UserCryptoDetails
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     '''
    #     This should return balance of the authenticated user
    #     '''
    #     user = self.request.user
    #     return Balance.objects.filter(balance=user)
