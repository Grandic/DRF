from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from course.models import Course
from course.validators import LinkValidator
from lesson.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='link')]



class LessonListSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'




