from rest_framework import viewsets
from course.paginators import CoursePaginator
from course.serializers import *


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    default_serializer = CourseSerializer
    pagination_class = CoursePaginator
    serializer_classes = {
        'list': CourseSerializer,
        'create': CourseCreateSerializer,
        'retrieve': CourseDetailSerializer,
        'update': CourseUpdateSerializer,
        'destroy': CourseDeleteSerializer
    }


    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def perform_create(self, serializer):
        new_instance = serializer.save()
        new_instance.user = self.request.user
        new_instance.save()



class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [AllowAny]