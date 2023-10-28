from django.db import models

from course.models import Course
from users.models import NULLABLE

class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='урок')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='categories/', verbose_name='превью (картинка)', **NULLABLE)
    link = models.URLField(max_length=300, verbose_name='ссылка на видео', **NULLABLE)
    сourse = models.ManyToManyField(Course)


    def __str__(self):
        return f'{self.name} {self.description} {self.сourse}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('name',)
