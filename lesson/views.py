from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from course.permissions import IsSuperUser, IsModerator, IsOwner
from lesson.models import Lesson
from lesson.serializers import LessonSerializer, LessonListSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonListSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator|IsOwner]

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator|IsOwner]

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]