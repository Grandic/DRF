from django.urls import path
from rest_framework.routers import DefaultRouter

from payments.apps import PaymentsConfig
from payments.views import PaymentViewSet, PaymentListAPIView, GetPaymentView, PaymentCreateAPIView

app_name = PaymentsConfig.name


router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [
                  path('list/', PaymentListAPIView.as_view(), name='payments-list'),
                  path('payments/<str:payment_id>/', GetPaymentView.as_view(), name='payments-get'),
                  path('create/', PaymentCreateAPIView.as_view(), name='payments-create'),
              ] + router.urls