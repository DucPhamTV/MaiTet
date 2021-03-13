from rest_framework.routers import SimpleRouter

from v1.items.views import ItemViewSet


router = SimpleRouter(trailing_slash=False)
router.register('items', ItemViewSet)
