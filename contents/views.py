from django.views.generic import ListView
from contents.models import (
    Carousel_About,
    Carousel_Home,
    Who_we_are,
    Who_we_are_sub,
    Top_executive,
    Top_executive_body,
    Our_offering,
    Testimonial,
    Testimonial_body,
    AboutUs,
    FacebookLink,
    InstagramLink,
    HowToInvest,
    Footer,
)


class CarouselHomeView(ListView):
    ''' Contains content for Carousel Section in the home Page '''

    model = Carousel_Home

class CarouselAboutView(ListView):
    ''' Contains content for Carousel Section in the about Page '''

    model = Carousel_About

class WWAView(ListView):
    ''' Contains decription Data for Who_We_Are Section in the home Page '''

    model = Who_we_are

class WWASView(ListView):
    ''' Contains Content for Who_We_Are Section in the home Page '''

    model = Who_we_are_sub

class TopExecutiveView(ListView):
    ''' Contains description Content for Top Investor Section in the home Page '''

    model = Top_executive


class TopExecutiveBodyView(ListView):
    ''' Contains Content for Top Executive Section in the home Page '''

    model = Top_executive_body

class OurOfferingView(ListView):
    ''' Contains Content for Our Offering Section in the home Page '''

    model = Our_offering


class TestimonialView(ListView):
    ''' Contains Description for Testimonial Section in the About Page '''

    model = Testimonial


class TestimonialBodyView(ListView):
    ''' Contains Content for Testimonial Section in the home Page '''

    model = Testimonial_body

class AboutUSView(ListView):
    ''' Contains Content for About US Section in the About Page '''

    model = AboutUs

class FBView(ListView):
    ''' Link to Facebook account '''

    model = FacebookLink

class IGView(ListView):
    ''' Link to Facebook account '''

    model = InstagramLink

class HTIView(ListView):
    ''' How to Invest Section '''

    model = HowToInvest

class FooterView(ListView):
    ''' Footer Content '''

    model = Footer