from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from payments.models import Payments
from users.models import User


class Userserializer(serializers.ModelSerializer):
    payment = SerializerMethodField()

    def get_payment(self, user):
        return [pay.payment_date for pay in Payments.objects.filter(user=user)]

    # def get_payment(self, user):
    #     return Payments.objects.filter(user=user)

    class Meta:
        model = User
        fields = '__all__'
