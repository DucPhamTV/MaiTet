from rest_framework.routers import SimpleRouter

from v1.users.views import UserViewSet

router = SimpleRouter(trailing_slash=False)
router.register('users', UserViewSet)
# router.register('authent', include('djoser.urls'), basename='theuser')
# router.register('authent', include('djoser.urls.authtoken'), basename='token')
# router.register('authent', include('djoser.urls.jwt'), basename='jwt')
