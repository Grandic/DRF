from rest_framework import viewsets
from users.models import User
from users.serializers import Userserializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = Userserializer
    queryset = User.objects.all()

