from rest_framework.serializers import ModelSerializer, StringRelatedField

from v1.addresses.models.addresses import Address


class AddressSerializer(ModelSerializer):
    province = StringRelatedField()
    district = StringRelatedField()
    ward = StringRelatedField()
    class Meta:
        model = Address
        fields = '__all__'

