from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from transactions.models import Deposit, Withdraw
from transactions.serializers import (
    DepositHistorySerializer,
    WithdrawSerializer,
    DepositFormSerializer,
)


class DepositView(generics.CreateAPIView):
    """
    This class handles the deposit request form
    """

    permission_classes = [IsAuthenticated]
    queryset = Deposit
    serializer_class = DepositFormSerializer


class DepositHistoryView(generics.ListAPIView):
    """
    This class displays the deposit history for a user
    """

    permission_classes = [IsAuthenticated]
    serializer_class = DepositHistorySerializer

    def get_queryset(self):
        """
        This should return Deposit History of the authenticated user
        """
        user = self.request.user
        return Deposit.objects.filter(user=user)


class WithdrawView(generics.CreateAPIView):
    """
    This class handles the form for withdraw request
    """

    permission_classes = [IsAuthenticated]
    queryset = Withdraw
    serializer_class = WithdrawSerializer


class WithdrawHistory(generics.ListAPIView):
    """
    This class handles the response for viewing withdraw history
    """

    serializer_class = WithdrawSerializer

    def get_queryset(self):
        """
        This should return Withdraw History of the authenticated user
        """
        user = self.request.user
        return Withdraw.objects.filter(user=user)
