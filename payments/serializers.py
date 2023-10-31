from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from payments.models import Payments


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'
        permission_classes = [IsAuthenticated]
