from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from course.models import Course, Subscription
from lesson.models import Lesson
@shared_task
def subscription_mailing(pk, model):
    try:
        if model == "Course":
            course = Course.objects.filter(pk=pk).first()
        else:
            lesson = Lesson.objects.filter(pk=pk).first()
            course = lesson.course

        subscriptions = Subscription.objects.filter(is_active=True, course=course)
        users = []

        for subscription in subscriptions:
            users.append(subscription.user)

        for user in users:
            send_mail(
                subject='Новая информация о вашей подписке!',
                message=f'Обновлены материалы для курса {course.name}!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email]
            )

    except Exception as e:
        print(f"Ошибка: {str(e)}")