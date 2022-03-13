from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from investments.models import Investment, Package
from investments.serializers import InvestmentFormSerializer, PackageFormSerializer

class InvestView(generics.CreateAPIView):
    '''
    This class displays the investment form
    '''
    permission_classes = [IsAuthenticated]
    queryset = Investment
    serializer_class = InvestmentFormSerializer

class PackageView(generics.CreateAPIView):
    '''
    This class displays the investment form
    '''
    permission_classes = [IsAdminUser]
    queryset = Package.objects.all()
    serializer_class = PackageFormSerializer