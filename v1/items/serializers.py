from rest_framework.serializers import ModelSerializer

from v1.items.models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = (
            'uuid',
            'created_by',
            'created_date',
            'modified_date',
        )
