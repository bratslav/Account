from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    language = models.ForeignKey(Langv, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()