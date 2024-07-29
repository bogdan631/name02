from django.shortcuts import render
from django.http import HttpResponse
from .models import Table
# Create your views here.
def home (request):

    return render(request,'main/home.html')

def test (request):
    table=Table.objects.all()
    return render(request,'main/test.html',{'table':table})