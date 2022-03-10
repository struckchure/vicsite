from rest_framework import generics
from investments.models import Investment, Package
from investments.serializers import InvestmentFormSerializer, PackageFormSerializer

class InvestView(generics.CreateAPIView):
    '''
    This class displays the investment form
    '''
    queryset = Investment.objects.all()
    serializer_class = InvestmentFormSerializer

class PackageView(generics.CreateAPIView):
    '''
    This class displays the investment form
    '''
    queryset = Package.objects.all()
    serializer_class = PackageFormSerializer