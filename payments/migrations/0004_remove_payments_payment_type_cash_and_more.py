# Generated by Django 4.2.6 on 2023-11-11 10:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_payments_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='payment_type_cash',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='payment_type_credit_card',
        ),
        migrations.AddField(
            model_name='payments',
            name='customer_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='payments',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='оплачено'),
        ),
        migrations.AddField(
            model_name='payments',
            name='pay_method',
            field=models.CharField(choices=[('card', 'картой'), ('cash', 'наличные')], default='cash', max_length=10, verbose_name='способ оплаты'),
        ),
        migrations.AddField(
            model_name='payments',
            name='status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='payments',
            name='stripe_id',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='payments',
            name='uid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True),
        ),
    ]