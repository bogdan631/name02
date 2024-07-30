from django.db import models

# Create your models here.
class Table(models.Model):
    title = models.CharField('название',max_length=50, default="Untilted")
    text = models.TextField('описание')
    def __str__(self):
        return self.title
    class Meta():
        verbose_name ='фильм'
        verbose_name_plural ='фильмы'

