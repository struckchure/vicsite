from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, CreateView
from accounts.models import Contact


# Create your views here.

class ContactView(CreateView):
    ''' Contact us Form '''
    model = Contact
    fields = "__all__"
