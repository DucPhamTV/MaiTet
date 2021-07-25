from rest_framework_nested.relations import NestedHyperlinkedRelatedField
from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    HyperlinkedRelatedField,
)

from v2.tracker.models import Tracker
from v2.tracker.tasks import crawl


class TrackerSerializer(ModelSerializer):
    created_by = SlugRelatedField(read_only=True, slug_field='username')
    # Change to nested relationship
    # result = HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='results-detail',
    # )
    result = NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='tracker-results-detail',
        parent_lookup_kwargs={'tracker_pk': 'tracker__pk'},
    )

    class Meta:
        model = Tracker
        fields = (
            'uuid',
            'created_date',
            'modified_date',
            'status',
            'created_by',
            'description',
            'url',
            'target',
            'check_interval',
            'webhook',
            'result',
        )

        read_only_fields = (
            'uuid',
            'created_date',
            'modified_date',
            'status',
            'created_by',
            'result',
        )
        ordering = ['-modified_date']

    def create(self, validated_data):
        print(validated_data)
        instance = super().create(validated_data)
        crawl.delay(instance.uuid)
        return instance
