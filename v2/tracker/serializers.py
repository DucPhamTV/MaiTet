from rest_framework.serializers import ModelSerializer, SlugRelatedField

from v2.tracker.models import Tracker
from v2.tracker.tasks import crawl

class TrackerSerializer(ModelSerializer):
    created_by = SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Tracker
        fields = '__all__'
        read_only_fields = (
            'uuid',
            'created_date',
            'modified_date',
            'status',
            'created_by',
        )
        ordering = ['-modified_date']

    def create(self, validated_data):
        print(validated_data)
        instance = super().create(validated_data)
        crawl.delay(instance.uuid)
        return instance
