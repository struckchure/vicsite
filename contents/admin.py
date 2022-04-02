from django.contrib import admin
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


admin.site.register(Carousel_Home)
admin.site.register(Carousel_About)
admin.site.register(Who_we_are)
admin.site.register(Who_we_are_sub)
admin.site.register(Top_executive)
admin.site.register(Top_executive_body)
admin.site.register(Our_offering)
admin.site.register(Testimonial)
admin.site.register(Testimonial_body)
admin.site.register(AboutUs)
admin.site.register(FacebookLink)
admin.site.register(InstagramLink)
admin.site.register(HowToInvest)
admin.site.register(Footer)