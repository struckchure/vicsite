from django.urls import path
from contents.views import (
    CarouselHomeView,
    CarouselAboutView,
    WWAView,
    WWASView,
    TopExecutiveView,
    TopExecutiveBodyView,
    OurOfferingView,
    TestimonialView,
    TestimonialBodyView,
    AboutUSView,
)


urlpatterns = [
    path('carousel-home', CarouselHomeView.as_view()),
    path('carousel-about', CarouselAboutView.as_view()),
    path('wwa', WWAView.as_view()),
    path('wwas', WWASView.as_view()),
    path('top-executive', TopExecutiveView.as_view()),
    path('top-executive-body', TopExecutiveBodyView.as_view()),
    path('our-offering', OurOfferingView.as_view()),
    path('testimonial', TestimonialView.as_view()),
    path('testimonial-body', TestimonialBodyView.as_view()),
    path('about-us', AboutUSView.as_view()),
]
