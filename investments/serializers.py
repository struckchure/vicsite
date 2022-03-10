from rest_framework import serializers
from investments.models import Investment

class InvestmentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = ('package', 'amount',)