# Generated by Django 4.2.6 on 2023-11-11 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_alter_payments_payment_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payments',
            options={'ordering': ('payment_date',), 'verbose_name': 'payment', 'verbose_name_plural': 'payments'},
        ),
    ]
