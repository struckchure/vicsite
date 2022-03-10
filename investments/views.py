from rest_framework import generics
from investments.models import Investment
from investments.serializers import InvestmentFormSerializer

class InvestView(generics.CreateAPIView):
    '''
    This class displays the investment form
    '''
    queryset = Investment.objects.all()
    serializer_class = InvestmentFormSerializer