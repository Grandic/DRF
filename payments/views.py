from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
import stripe
from rest_framework.response import Response
from rest_framework.views import APIView
from config.settings import STRIPE_SECRET_KEY
from payments.models import Payments
from payments.serializers import PaymentSerializer



class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save()
        payment.user = self.request.user
        payment.save()
        return super().perform_create(serializer)


class PaymentCreateAPIView(generics.CreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save()
        stripe.api_key = STRIPE_SECRET_KEY
        pay = stripe.PaymentIntent.create(
            amount=payment.count,
            currency="rub",
            automatic_payment_methods={"enabled": True},
        )
        pay.save()
        return super().perform_create(serializer)


class GetPaymentView(APIView):
    def get(self, request, payment_id):
        stripe.api_key = STRIPE_SECRET_KEY
        payment_intent = stripe.PaymentIntent.retrieve(payment_id)
        return Response({
            'status': payment_intent.status,
            'body': payment_intent})


class PaymentListAPIView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('pay_method',)
    ordering_fields = ['payment_date']