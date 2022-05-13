from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from accounts.models import Contact

class HomePageView(TemplateView):
    template_name = "front/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["carousel_home"] = Carousel_Home.objects.all()
        context = {
            "package": Package.objects.all(),
            "HTI": HowToInvest.objects.all(),
            "aboutus": AboutUs.objects.all(),
            "our_offering": Our_offering.objects.all(),
            "who_we_are": Who_we_are(),
            "carousel_home": Carousel_Home.objects.all(),
        }
        return context

class AboutPage(CreateView):
    model = Contact
    fields = "__all__"
    success_url = reverse_lazy("about_us")
    template_name = "front/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["carousel_home"] = Carousel_Home.objects.all()
        context = {
            "package": Package.objects.all(),
            "HTI": HowToInvest.objects.all(),
            "aboutus": AboutUs.objects.all(),
            "our_offering": Our_offering.objects.all(),
            "who_we_are": Who_we_are(),
            "carousel_home": Carousel_Home.objects.all(),
        }
        return context
