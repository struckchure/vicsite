from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from accounts.models import Contact
from transactions.models import Deposit, Package
from contents.models import Carousel_Home, Carousel_About, Who_we_are, Who_we_are_sub, Top_executive, Top_executive_body, Our_offering, AboutUs, Footer, HowToInvest
import requests

api_url = "https://newsdata.io/api/1/news?apikey=pub_5728afbaab86b03fb74978dc8d4c5f16e07c&q=crypto&country=in,gb,us&language=en"
response = requests.get(api_url)[:4]

class HomePageView(TemplateView):
    template_name = "front/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = 
        # context["carousel_home"] = Carousel_Home.objects.all()
        context = {
            "package": Package.objects.all(),
            "HTI": HowToInvest.objects.all(),
            "aboutus": AboutUs.objects.all(),
            "our_offering": Our_offering.objects.all(),
            "who_we_are": Who_we_are(),
            "carousel_home": Carousel_Home.objects.all(),
            "blog": blog,
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
        Who_we_are_sub = Who_we_are_sub.objects.all()
        context = {
            "package": Package.objects.all(),
            "how_to_invest": HowToInvest.objects.all(),
            "aboutus": AboutUs.objects.all(),
            "our_offering": Our_offering.objects.all(),
            "wwe": Who_we_are_sub.objects.get(id=1),
            "carousel_home": Carousel_Home.objects.all(),
        }
        return context
