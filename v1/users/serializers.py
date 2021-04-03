from rest_framework.serializers import ModelSerializer

from v1.users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'phone']
