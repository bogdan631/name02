from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Table
from .forms import FilmForm

def home (request):
    pass

def test (request):
    table=Table.objects.all()


def newfilm(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/test')
        else:
            return render(request, 'main/new-film.html', {'form': form})
    else:
        form = FilmForm()


