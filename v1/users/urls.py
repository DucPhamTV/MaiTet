# from rest_framework.routers import SimpleRouter
# from django.urls import include
#
# from v1.users.views import UserViewSet

# router = SimpleRouter(trailing_slash=False)
# router.register('users', UserViewSet, basename='myuser')
# router.register('authen', include('djoser.urls'), basename='theuser')
# router.register('authen', include('djoser.urls.authtoken'), basename='token')
# router.register('authen', include('djoser.urls.jwt'), basename='jwt')

from django.conf.urls import url, include

user_urlpatterns = [
    url(r'^api/v1/', include('djoser.urls')),
    url(r'^api/v1/', include('djoser.urls.authtoken')),
]
