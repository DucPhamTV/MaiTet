from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from v2.results.serializers import ResultSerializer
from v2.results.models import Result
# Create your views here.


class ResultViewSet(ReadOnlyModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # return self.queryset.filter(tracker__pk=self.request.)
        return self.queryset
