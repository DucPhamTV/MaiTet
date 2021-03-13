
from django.urls import include, path
from rest_framework import routers
from v1.users.views import UserViewSet
from v1.items.views import ItemViewSet
from v1.comments.views import CommentViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'items', ItemViewSet)
router.register(r'comments', CommentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
