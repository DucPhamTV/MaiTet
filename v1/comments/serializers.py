from rest_framework.serializers import HyperlinkedModelSerializer

from v1.comments.models import Comment


class CommentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
