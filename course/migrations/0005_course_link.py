# Generated by Django 4.2.6 on 2023-11-05 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_course_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='link',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='ссылка на видео'),
        ),
    ]
