from django.shortcuts import render
from django.http import HttpResponse
from .models import Table
# Create your views here.
def home (request):
    table =Table.objects.all()
    return render(request,'main/home.html',{'table':table})