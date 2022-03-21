from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from investments.models import Investment, Package
from investments.serializers import InvestmentFormSerializer, PackageFormSerializer, InvestmentHistorySerializer
from accounts.models import CustomUser


class InvestView(generics.CreateAPIView):
    """
    This class displays the investment form
    """

    permission_classes = [IsAuthenticated]
    queryset = Investment
    serializer_class = InvestmentFormSerializer

    def post(self, request):
        user = get_object_or_404(CustomUser, pk=request.user.pk)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["user"]= user
        serializer.save()
        return Response({
            "message": "success",
        }, status=status.HTTP_200_OK)

class InvestHistoryView(generics.ListAPIView):
    """
    This class displays the investment History
    """

    permission_classes = [IsAuthenticated]
    queryset = Investment.objects.all()
    serializer_class = InvestmentHistorySerializer


class PackageView(generics.ListAPIView):
    """
    This class displays the Investment Packages
    """

    queryset = Package.objects.all()
    serializer_class = PackageFormSerializer
    permission_classes = [IsAuthenticated]
