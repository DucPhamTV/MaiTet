from rest_framework.serializers import HyperlinkedModelSerializer

from v1.items.models import Item


class ItemSerializer(HyperlinkedModelSerializer):
    class Meta:
         model = Item
         exclude = ['address']
