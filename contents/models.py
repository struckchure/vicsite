from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField


class Carousel_Home(models.Model):              # Contents in the first carousel home section
    heading_one = RichTextField()
    heading_two = RichTextField()

class Carousel_About(models.Model):             # Contents in the second carousel section  in the about us section
    heading_one = RichTextField()
    heading_two = RichTextField()

class Who_we_are(models.Model):
    text = RichTextField()     # Text directly under the Who we are section

class Who_we_are_sub(models.Model):             # The contents in the boxed sub section under who we are
    title = RichTextField()
    msg = RichTextField()

class Top_executive(models.Model):
    text = RichTextField()     # Text directly under the Who we are section

class Top_executive_body(models.Model):
    pics =  CloudinaryField('image')
    name = models.CharField(max_length=80)
    position = models.CharField(max_length=80)

class Our_offering(models.Model):
    icon = models.CharField(max_length=50)
    title = RichTextField()
    msg = RichTextField()

class Testimonial(models.Model):
    text = RichTextField()     # The text directly under the section ttitle

class Testimonial_body(models.Model):
    pics = CloudinaryField('image')
    name = models.CharField(max_length=100)
    comments = RichTextField()

class AboutUs(models.Model):
    msg = RichTextField() #  Contents are huge