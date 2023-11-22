from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Mark(TemplateView):
    template_name = 'index.html'

class Zucerberg(TemplateView):
    template_name = 'mark.html'
    