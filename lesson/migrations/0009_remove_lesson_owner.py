# Generated by Django 4.2.6 on 2023-11-05 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0008_alter_lesson_course_alter_lesson_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='owner',
        ),
    ]
