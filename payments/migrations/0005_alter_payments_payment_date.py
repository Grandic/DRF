# Generated by Django 4.2.6 on 2023-11-11 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_remove_payments_payment_type_cash_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateField(default=django.utils.timezone.now, max_length=100, verbose_name='дата оплаты'),
        ),
    ]
