from rest_framework.serializers import ModelSerializer

from v2.results.models import Result


class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
        ordering = ['-modified_date']
