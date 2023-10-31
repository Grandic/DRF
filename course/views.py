from rest_framework import viewsets
from course.permissions import IsOwnerorStaff
from course.serializers import *


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    default_serializer = CourseSerializer
    permission_classes = [IsOwnerorStaff]
    serializer_classes = {
        'list': CourseSerializer,
        'retrieve': CourseDetailSerializer,
    }


    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)