from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.permissions import IsAuthenticated

from course.models import Course
from lesson.models import Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons_quantity = SerializerMethodField()

    def get_lessons_quantity(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = '__all__'
        permission_classes = [IsAuthenticated]

class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_in_course = SerializerMethodField()

    def get_lessons_in_course(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = '__all__'
        permission_classes = [IsAuthenticated]