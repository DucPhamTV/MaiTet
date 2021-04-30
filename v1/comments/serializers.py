from rest_framework.serializers import ModelSerializer

from v1.comments.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = (
            'uuid',
            'written_by',
            'created_date',
            'modified_date',
        )
