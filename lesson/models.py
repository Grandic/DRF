from django.conf import settings
from django.db import models
from course.models import Course
from users.models import NULLABLE, User


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='урок')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='lessons/', verbose_name='превью (картинка)', **NULLABLE)
    link = models.URLField(max_length=300, verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description} {self.course}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('name',)
