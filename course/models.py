from django.conf import settings
from django.db import models
from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='курс')
    image = models.ImageField(upload_to='courses/', verbose_name='превью (картинка)', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('name',)
