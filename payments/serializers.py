from rest_framework import serializers
from stripe.api_resources.payment_intent import PaymentIntent

from payments.models import Payments


class PaymentSerializer(serializers.ModelSerializer):
    pay = PaymentIntent.stripe_id

    class Meta:
        model = Payments
        fields = '__all__'