from rest_framework import viewsets
from payments.models import Payments
from payments.serializers import PaymentSerializer


class PaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()