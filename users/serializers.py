from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.permissions import IsAuthenticated

from course.permissions import IsModerator, IsOwner, IsSuperUser
from lesson.models import Lesson
from payments.models import Payments
from users.models import User


class Userserializer(serializers.ModelSerializer):
    payment = SerializerMethodField()

    def get_payment(self, user):
        return [pay.payment_date for pay in Payments.objects.filter(user=user)]

    class Meta:
        model = User
        fields = '__all__'
        permission_classes = [IsAuthenticated]

class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        permission_classes = [IsAuthenticated, IsModerator | IsOwner]

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        permission_classes = [IsAuthenticated, IsSuperUser]

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        permission_classes = [IsOwner]

class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        permission_classes = [IsAuthenticated, IsOwner]

