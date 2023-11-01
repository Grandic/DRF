from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from users.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    default_serializer = Userserializer
    queryset = User.objects.all()
    serializer_classes = {
        'create': UserCreateSerializer,
        'retrieve': UserDetailSerializer,
        'update': UserUpdateSerializer,
        'destroy': UserDeleteSerializer
    }
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)