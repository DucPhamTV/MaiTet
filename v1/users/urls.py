from rest_framework.routers import SimpleRouter

from v1.users.views import UserViewSet

router = SimpleRouter(trailing_slash=False)
router.register('users', UserViewSet)
