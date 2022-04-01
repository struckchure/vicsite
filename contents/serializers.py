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
    FacebookLink,
    InstagramLink,
)


class CarouselAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel_About
        fields = "__all__"

class CarouselHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel_Home
        fields = "__all__"

# Who_We_Are Model
class WWASerializer(serializers.ModelSerializer):
    class Meta:
        model = Who_we_are
        fields = "__all__"

# Who_We_Are_Sub Model
class WWESSerializer(serializers.ModelSerializer):
    class Meta:
        model = Who_we_are_sub
        fields = "__all__"

class TopExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Top_executive
        fields = "__all__"

class TopExecutiveBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Top_executive_body
        fields = "__all__"

class OurOfferingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_offering
        fields = "__all__"

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"

class TestimonialBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial_body
        fields = "__all__"

class AboutUSSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"

class FBSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookLink
        fields = "__all__"

class IGSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramLink
        fields = "__all__"