from rest_framework import serializers
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
)


class CarouselAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel_About.objects.all()
        fields = "__all__"

class CarouselHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel_Home.objects.all()
        fields = "__all__"

# Who_We_Are Model
class WWASerializer(serializers.ModelSerializer):
    class Meta:
        model = Who_we_are.objects.all()
        fields = "__all__"

# Who_We_Are_Sub Model
class WWESSerializer(serializers.ModelSerializer):
    class Meta:
        model = Who_we_are_sub.objects.all()
        fields = "__all__"

class TopExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Top_executive.objects.all()
        fields = "__all__"

class TopExecutiveBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Top_executive_body.objects.all()
        fields = "__all__"

class OurOfferingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_offering.objects.all()
        fields = "__all__"

class TestimonialSerializer(serializers.ModelSerializer):
    model = Testimonial.objects.all()
    fields = "__all__"

class TestimonialBodySerializer(serializers.ModelSerializer):
    model = Testimonial_body.objects.all()
    fields = "__all__"

class AboutUSSerializer(serializers.ModelSerializer):
    model = AboutUs.objects.all()
    fields = "__all__"