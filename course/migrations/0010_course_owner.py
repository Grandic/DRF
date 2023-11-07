# Generated by Django 4.2.6 on 2023-11-07 16:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0009_alter_course_description_alter_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='owner',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]