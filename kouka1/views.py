from django.shortcuts import render

# Create your views here.
from django.views import generic
from.forms import Kouka1Form

class Kouka1View(generic.FormView):
    template_name="kouka1.html"
    form_class=Kouka1Form

