from django.db import models

# Create your models here.
class Table(models.Model):
    name = models.CharField('название',max_length=20)
    text = models.TextField('описание')
    def __str__(self):
        return self.name
    class Meta():
        verbose_name ='фильм'
        verbose_name_plural ='фильмы'

