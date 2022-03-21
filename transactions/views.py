from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from transactions.models import Deposit, Withdraw
from transactions.serializers import (
    DepositHistorySerializer,
    WithdrawSerializer,
    DepositFormSerializer,
)
from accounts.models import CustomUser


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


class WithdrawHistory(generics.GenericAPIView):
    """
    This class handles the response for viewing withdraw history
    """

    serializer_class = WithdrawSerializer

    def get(self, request):
        """
        This should return Withdraw History of the authenticated user
        """
        user = get_object_or_404(CustomUser, pk=request.user.pk)
        his = get_object_or_404(Withdraw, user=user)
        print(user)
        serializer = self.serializer_class(instance=his)
        return Response(serializer.data, status = status.HTTP_200_OK)
