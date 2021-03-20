from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from v1.users.urls import router as user_router
from v1.items.urls import router as item_router
from v1.comments.urls import router as comment_router
from v1.addresses.urls import router as address_router

router = routers.DefaultRouter()

router.registry.extend(user_router.registry)
router.registry.extend(item_router.registry)
router.registry.extend(comment_router.registry)
router.registry.extend(address_router.registry)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('auth/', include("djoser.urls")),
    #path('auth/', include('djoser.urls.authtoken')),
    url(r'^authen/', include('djoser.urls')),
    url(r'^authen/', include('djoser.urls.authtoken')),
    url(r'^authen/', include('djoser.urls.jwt')),
]
