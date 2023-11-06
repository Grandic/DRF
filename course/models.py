from django.db import models
from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='курс')
    image = models.ImageField(upload_to='courses/', verbose_name='превью (картинка)', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    price = models.PositiveIntegerField(default=0, verbose_name='стоимость', **NULLABLE)
    link = models.URLField(max_length=300, verbose_name='ссылка на видео', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('name',)



class Subscription(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='подписка')

    def __str__(self):
        return f'{self.is_active}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'