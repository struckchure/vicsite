from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser, Balance, UserCryptoDetails, Coin, CoinAddress
from accounts.serializers import UserBalanceSerializer, UserCryptoDetailsSerializer, CoinOption, CoinAddressSerializer

# Create your views here.
class UserBalanceView(generics.GenericAPIView):
    """
    Returns User Balance
    """

    serializer_class = UserBalanceSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        This should return balance of the authenticated user
        """
        user = get_object_or_404(CustomUser, pk=request.user.pk)
        bal = get_object_or_404(Balance, user=user)
        serializer = self.serializer_class(instance=bal)
        return Response(serializer.data, status = status.HTTP_200_OK)


class UserAsset(generics.CreateAPIView):
    """
    Creates User Asset Details. Edit List
    """

    queryset = UserCryptoDetails
    serializer_class = UserCryptoDetailsSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     '''
    #     This should return balance of the authenticated user
    #     '''
    #     user = self.request.user
    #     return user.Balance.all()


class UserAssetView(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns User Asset Details, Edit and delete..
    """

    queryset = UserCryptoDetails
    serializer_class = UserCryptoDetailsSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     '''
    #     This should return balance of the authenticated user
    #     '''
    #     user = self.request.user
    #     return user.Balance.all()

class CoinOptionView(generics.ListAPIView):
    ''' Returns a list of coin/wallet '''

    queryset = Coin.objects.all()
    serializer_class = CoinOption
    permission_classes = [IsAuthenticated]
    

class CoinAddressView(generics.RetrieveAPIView):
    ''' Returns the coin address '''

    queryset = CoinAddress
    serializer_class = CoinAddressSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, coin_id):
        coin = get_object_or_404(Coin, pk=coin_id)
        coin_address = get_object_or_404(CoinAddress, coin=coin)
        serializer = self.serializer_class(instance=coin_address)
        return Response(serializer.data, status = status.HTTP_200_OK)



