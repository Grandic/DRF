from rest_framework import viewsets
from course.serializers import *


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    default_serializer = CourseSerializer
    serializer_classes = {
        'list': CourseSerializer,
        'create': CourseCreateSerializer,
        'retrieve': CourseDetailSerializer,
        'update': CourseUpdateSerializer,
        'destroy': CourseDeleteSerializer
    }


    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)