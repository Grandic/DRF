from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.permissions import IsAuthenticated

from course.models import Course, Subscription
from course.permissions import IsSuperUser, IsModerator, IsOwner
from course.validators import LinkValidator
from lesson.models import Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons_quantity = SerializerMethodField()

    def get_lessons_quantity(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = '__all__'
        permission_classes = [IsAuthenticated, IsSuperUser | IsModerator | IsOwner]

class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_in_course = SerializerMethodField()
    active_sub = SerializerMethodField()

    def get_lessons_in_course(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    def get_active_sub(self, course):
        return [sub.is_active for sub in Subscription.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = '__all__'
        permission_classes = [IsAuthenticated, IsSuperUser | IsModerator | IsOwner]

class CourseCreateSerializer(serializers.ModelSerializer):
    link = serializers.URLField(validators=[LinkValidator])

    class Meta:
        model = Course
        fields = '__all__'
        permission_classes = [IsAuthenticated, IsSuperUser]

class CourseUpdateSerializer(serializers.ModelSerializer):
    link = serializers.URLField(validators=[LinkValidator])

    class Meta:
        model = Course
        fields = '__all__'
        permission_classes = [IsAuthenticated, IsSuperUser | IsModerator | IsOwner]

class CourseDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        permission_classes = [IsAuthenticated, IsSuperUser]


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
        permission_classes = [IsAuthenticated, IsSuperUser | IsModerator | IsOwner]