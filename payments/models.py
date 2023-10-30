from django.db import models
from course.models import Course
from lesson.models import Lesson
from users.models import User, NULLABLE

class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateField(max_length=100, verbose_name='дата оплаты')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,  **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,  **NULLABLE)
    count = models.CharField(max_length=100, verbose_name='сумма оплаты')
    payment_type_cash = models.BooleanField(default=False, verbose_name='оплата наличными')
    payment_type_credit_card = models.BooleanField(default=False, verbose_name='оплата картой')

    def __str__(self):
        return f'{self.user} {self.payment_date} {self.count}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ('payment_date',)
