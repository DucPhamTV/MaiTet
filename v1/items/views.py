# from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from v1.items.serializers import ItemSerializer
from v1.items.models import Item


class ItemViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
