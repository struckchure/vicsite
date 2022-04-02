from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField


class Carousel_Home(models.Model):              # Contents in the first carousel home section
    heading_one = RichTextField()
    heading_two = RichTextField()

    def __str__(self):
        return self.heading_one[:20]


class Carousel_About(models.Model):             # Contents in the second carousel section  in the about us section
    heading_one = RichTextField()
    heading_two = RichTextField()

    def __str__(self):
        return self.heading_one[:15]

class Who_we_are(models.Model):
    text = RichTextField()     # Text directly under the Who we are section

    def __str__(self):
        return self.text[:20]

class Who_we_are_sub(models.Model):             # The contents in the boxed sub section under who we are
    title = RichTextField()
    msg = RichTextField()

    def __str__(self):
        return self.title[:20]

class Top_executive(models.Model):
    text = RichTextField()     # Text directly under the Who we are section

    def __str__(self):
        return self.text[:30]

class Top_executive_body(models.Model):
    pics =  CloudinaryField('image')
    name = models.CharField(max_length=80)
    position = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Our_offering(models.Model):
    icon = models.CharField(max_length=50)
    title = RichTextField()
    msg = RichTextField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    text = RichTextField()     # The text directly under the section title

    def __str__(self):
        return self.text

class Testimonial_body(models.Model):
    pics = CloudinaryField('image')
    name = models.CharField(max_length=100)
    comments = RichTextField()

    def __str__(self):
        return self.name

class AboutUs(models.Model):
    msg = RichTextField() #  Contents are huge

    def __str__(self):
        return self.msg[:20]
    
class FacebookLink(models.Model):
    link = models.CharField(max_length=300)

class InstagramLink(models.Model):
    link = models.CharField(max_length=300)

class HowToInvest(models.Model):
    title_one = models.CharField(max_length=500)
    content_one = RichTextField()

class Footer(models.Model):
    msg = RichTextField()