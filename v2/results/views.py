from django.shortcuts import render

from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from v2.results.serializers import ResultSerializer
from v2.results.models import Result
# Create your views here.

class ResultViewSet(ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
