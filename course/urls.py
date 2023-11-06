from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from course.apps import CourseConfig
from rest_framework.routers import DefaultRouter
from course.views import *

app_name = CourseConfig.name


subscribe_list = SubscriptionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
subscribe_detail = SubscriptionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
urlpatterns = format_suffix_patterns([
    path('subscribe/', subscribe_list, name='subscribe-list'),
    path('subscribe/<int:pk>/', subscribe_detail, name='subscribe-detail'),
]) + router.urls