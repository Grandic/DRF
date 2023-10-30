# Generated by Django 4.2.6 on 2023-10-29 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_course_image'),
        ('lesson', '0004_rename_сourse_lesson_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='course',
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.course'),
            preserve_default=False,
        ),
    ]
