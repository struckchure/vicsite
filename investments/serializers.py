from rest_framework import serializers
from investments.models import Investment, Package


class InvestmentFormSerializer(serializers.ModelSerializer):
    """
    Form for choosing the Investment Package and the capital
    """

    class Meta:
        model = Investment
        fields = (
            "package",
            "amount",
        )

class InvestmentHistorySerializer(serializers.ModelSerializer):
    """
    Returns Investment History
    """

    class Meta:
        model = Investment
        fields = (
            "balance",
            "package",
            "amount",
            "status",
        )


class PackageFormSerializer(serializers.ModelSerializer):
    """
    Creation of Investment Package
    """

    class Meta:
        model = Package
        fields = (
            "id",
            "name",
            "maximum_stake",
            "minimum_stake",
            "roi",
            "duration",
        )
