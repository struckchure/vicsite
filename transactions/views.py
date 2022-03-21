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
    # queryset = Deposit
    serializer_class = DepositFormSerializer

    def post(self, request):
        user = get_object_or_404(CustomUser, pk=request.user.pk)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["user"]= user
        serializer.save()
        return Response({
            "message": "success",
        }, status=status.HTTP_200_OK)


class DepositHistoryView(generics.GenericAPIView):
    """
    This class displays the deposit history for a user
    """

    permission_classes = [IsAuthenticated]
    serializer_class = DepositHistorySerializer

    def get(self, request):
       """
       This should return Withdraw History of the authenticated user
       """
       user = get_object_or_404(CustomUser, pk=request.user.pk)
       dep =  Deposit.objects.filter(user=user)
       serializer = self.serializer_class(instance=dep, many=True)
       return Response(serializer.data, status = status.HTTP_200_OK)

class WithdrawView(generics.CreateAPIView):
    """
    This class handles the form for withdraw request
    """

    permission_classes = [IsAuthenticated]
    # queryset = Withdraw
    serializer_class = WithdrawSerializer

    def post(self, request):
        user = get_object_or_404(CustomUser, pk=request.user.pk)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["user"]= user
        serializer.save()
        return Response({
            "message": "success",
        }, status=status.HTTP_200_OK)



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
        his =  Withdraw.objects.filter(user=user)
        serializer = self.serializer_class(instance=his, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
