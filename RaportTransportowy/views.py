from django.shortcuts import render

from .models import Transport,Status

# Create your views here.
def index(request):
    return render(request,'RaportTransportowy/index.html')
