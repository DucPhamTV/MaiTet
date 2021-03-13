from rest_framework.serializers import HyperlinkedModelSerializer

from v1.users.models import User


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
         model = User
         fields = ['url', 'username', 'email', 'is_staff', 'phone']
