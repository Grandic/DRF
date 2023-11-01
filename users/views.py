from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from course.permissions import IsSuperUser
from users.models import User
from users.serializers import Userserializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = Userserializer
    queryset = User.objects.all()
    permission_classes = [IsSuperUser]

