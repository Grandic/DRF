# Generated by Django 4.2.6 on 2023-11-05 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('member', 'memeber'), ('moderator', 'moderator'), ('superuser', 'superuser')], default='member', max_length=9),
        ),
    ]
