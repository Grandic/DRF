from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from course.permissions import IsSuperUser
from payments.models import Payments
from payments.serializers import PaymentSerializer
from rest_framework.filters import OrderingFilter


class PaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated, IsSuperUser]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_type_cash',
                        'payment_type_credit_card')
    ordering_fields = ('payment_date',)