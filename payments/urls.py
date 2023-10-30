from payments.apps import PaymentsConfig
from rest_framework.routers import DefaultRouter
from payments.views import PaymentsViewSet

app_name = PaymentsConfig.name


router = DefaultRouter()
router.register(r'payments', PaymentsViewSet, basename='payments')

urlpatterns = [

] + router.urls