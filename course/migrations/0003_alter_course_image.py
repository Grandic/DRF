# Generated by Django 4.2.6 on 2023-10-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/', verbose_name='превью (картинка)'),
        ),
    ]
