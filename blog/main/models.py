from django.db import models


class Blog(models.Model):
    title = models.CharField('Название', max_length=150)
    text = models.TextField('Тескт', max_length=400)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
