# Generated by Django 4.2.6 on 2023-11-08 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_payments_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='count',
            field=models.IntegerField(blank=True, null=True, verbose_name='сумма оплаты'),
        ),
    ]
