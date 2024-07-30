from django.shortcuts import render
from django.http import HttpResponse
from .models import Table
from .forms import FilmForm
# Create your views here.
def home (request):

    return render(request,'main/home.html')

def test (request):
    table=Table.objects.all()
    return render(request,'main/test.html',{'table':table})

def new_film (request):
    form=FilmForm()
    return render(request, 'main/new film.html', {'form': form})