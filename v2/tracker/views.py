from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from v2.tracker.serializers import TrackerSerializer
from v2.tracker.models import Tracker


# Create your views here.
class TrackerViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        if self.request.user.is_anonymous:
            # For development, will be change to 401 Unauthorized.
            return self.queryset

        return self.queryset.filter(created_by=self.request.user)
