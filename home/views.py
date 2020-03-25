from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

def home(request):
    return render(request, 'home/homepage.html')
# Create your views here.
