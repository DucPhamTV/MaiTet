from rest_framework.routers import SimpleRouter

from v1.addresses.views import AddressViewSet

router = SimpleRouter(trailing_slash=False)
router.register('addresses', AddressViewSet)
