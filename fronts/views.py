from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from accounts.models import Contact
from transactions.models import Deposit, Package
from contents.models import Carousel_Home, Carousel_About, Who_we_are, Who_we_are_sub, Top_executive, Top_executive_body, Our_offering, AboutUs, Footer, HowToInvest



class HomePageView(TemplateView):
    template_name = "front/homes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        WHo_we_are_sub = Who_we_are_sub.objects.all()

        # context["carousel_home"] = Carousel_Home.objects.all()
        context = {
            "package": Package.objects.all(),
            "HTI": HowToInvest.objects.all(),
            "aboutus": AboutUs.objects.all(),
            "our_offering": Our_offering.objects.all(),
            "who_we_are": WHo_we_are_sub,
            "carousel_home": Carousel_Home.objects.all(),
            # "blog": response,
        }
        return context

class AboutPage(CreateView):
    model = Contact
    fields = "__all__"
    success_url = reverse_lazy("about_us")
    template_name = "front/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carousel_about = Carousel_About.objects.all()
        context = {
            "package": Package.objects.all(),
            "how_to_invest": HowToInvest.objects.all(),
            "aboutus": AboutUs.objects.all(),
            "our_offering": Our_offering.objects.all(),
            "carousel_about": carousel_about,
            # "form": Contact.objects.all(),
        }
        return context
