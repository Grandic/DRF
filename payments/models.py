import uuid
from django.utils.timezone import now as now
from django.db import models
from course.models import Course
from lesson.models import Lesson
from users.models import User, NULLABLE

class Payments(models.Model):
    PAY_CARD = 'card'
    PAY_CASH = 'cash'

    PAY_TYPES = (
        (PAY_CARD, 'картой'),
        (PAY_CASH, 'наличные')

    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)
    payment_date = models.DateField(max_length=100, verbose_name='дата оплаты', default=now)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,  **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,  **NULLABLE)
    count = models.IntegerField(verbose_name='сумма оплаты', **NULLABLE)


    #Stripe
    pay_method = models.CharField(choices=PAY_TYPES, default=PAY_CASH, max_length=10, verbose_name='способ оплаты')
    is_paid = models.BooleanField(default=False, verbose_name='оплачено')
    uid = models.UUIDField(default=uuid.uuid4, editable=False, **NULLABLE)
    stripe_id = models.CharField(max_length=255, unique=True, editable=False, **NULLABLE)
    status = models.CharField(max_length=10, **NULLABLE)
    customer_email = models.EmailField(**NULLABLE)


    def __str__(self):
        return f'{self.count} {self.pay_method}'

    class Meta:
        verbose_name = 'payment'
        verbose_name_plural = 'payments'
        ordering = ('payment_date',)

