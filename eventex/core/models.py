from django.db import models
from django.shortcuts import resolve_url as r


class Speaker(models.Model):
    name = models.CharField(max_length=255, verbose_name='nome')
    slug = models.SlugField(verbose_name='slug')
    photo = models.URLField(verbose_name='foto')
    website = models.URLField(verbose_name='website', blank=True)
    description = models.TextField(verbose_name='descrição', blank=True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)
