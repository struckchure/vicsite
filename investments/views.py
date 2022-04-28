from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from investments.models import Investment, Package
from accounts.models import CustomUser


class InvestView(ListView):
    """
    This class displays the investment form
    """
    model = Investment
    template_name = "investments/invest.html"
    # success_url = reverse_lazy("dashboard")

    extra_context = {
        "package": Package.objects.all()
    }

    # def post(self, request):
    #     user = get_object_or_404(CustomUser, pk=request.user.pk)
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.validated_data["user"]= user
    #     serializer.save()
    #     return Response({
    #         "message": "success",
    #     }, status=status.HTTP_200_OK)

# class PackageView(ListView):
#     """
#     This class displays the Investment Packages
#     """

#     model = Pa

