from django.db import models
from django.urls import reverse

class Langv(models.Model):
    title = models.CharField(max_length=255, verbose_name='Язык интерфейса')
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lang', kwargs={'slug': self.slug})



    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
        ordering = ['title']
