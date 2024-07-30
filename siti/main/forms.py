from .models import Table
from django.forms import ModelForm

class FilmForm(ModelForm):
    class Meta():
        model=Table
        fields=['name', 'text']