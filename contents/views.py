from rest_framework import generics
from rest_framework.permissions import AllowAny
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
)
from contents.serializers import (
    CarouselAboutSerializer,
    CarouselHomeSerializer,
    WWASerializer,
    WWESSerializer,
    TopExecutiveSerializer,
    TopExecutiveBodySerializer,
    OurOfferingSerializer,
    TestimonialSerializer,
    TestimonialBodySerializer,
    AboutUSSerializer,
    FBSerializer,
    IGSerializer,
)


class CarouselHomeView(generics.ListAPIView):
    ''' Contains content for Carousel Section in the home Page '''

    queryset = Carousel_Home.objects.all()
    serializer_class = CarouselHomeSerializer
    permission_classes =[AllowAny]

class CarouselAboutView(generics.ListAPIView):
    ''' Contains content for Carousel Section in the about Page '''

    queryset = Carousel_About.objects.all()
    serializer_class = CarouselAboutSerializer
    permission_classes =[AllowAny]

class WWAView(generics.ListAPIView):
    ''' Contains decription Data for Who_We_Are Section in the home Page '''

    queryset = Who_we_are.objects.all()
    serializer_class = WWASerializer
    permission_classes = [AllowAny]

class WWASView(generics.ListAPIView):
    ''' Contains Content for Who_We_Are Section in the home Page '''

    queryset = Who_we_are_sub.objects.all()
    serializer_class = WWESSerializer
    permission_classes = [AllowAny]

class TopExecutiveView(generics.ListAPIView):
    ''' Contains description Content for Top Investor Section in the home Page '''

    queryset = Top_executive.objects.all()
    serializer_class = TopExecutiveSerializer
    permission_classes = [AllowAny]

class TopExecutiveBodyView(generics.ListAPIView):
    ''' Contains Content for Top Executive Section in the home Page '''

    queryset = Top_executive_body.objects.all()
    serializer_class = TopExecutiveBodySerializer
    permission_classes = [AllowAny]

class OurOfferingView(generics.ListAPIView):
    ''' Contains Content for Our Offering Section in the home Page '''

    queryset = Our_offering.objects.all()
    serializer_class = OurOfferingSerializer
    permission_classes = [AllowAny]

class TestimonialView(generics.ListAPIView):
    ''' Contains Description for Testimonial Section in the About Page '''

    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [AllowAny]

class TestimonialBodyView(generics.ListAPIView):
    ''' Contains Content for Testimonial Section in the home Page '''

    queryset = Testimonial_body.objects.all()
    serializer_class = TestimonialBodySerializer
    permission_classes = [AllowAny]

class AboutUSView(generics.ListAPIView):
    ''' Contains Content for About US Section in the About Page '''

    queryset = AboutUs.objects.all()
    serializer_class = AboutUSSerializer
    permission_classes = [AllowAny]

class FBView(generics.ListAPIView):
    ''' Link to Facebook account '''

    queryset = FacebookLink.objects.all()
    serializer_class = FBSerializer
    permission_classes = [AllowAny]

class IGView(generics.ListAPIView):
    ''' Link to Facebook account '''

    queryset = InstagramLink.objects.all()
    serializer_class = IGSerializer
    permission_classes = [AllowAny]