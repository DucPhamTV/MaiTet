from rest_framework.serializers import ModelSerializer

from v2.tracker.models import Tracker

class TrackerSerializer(ModelSerializer):
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
