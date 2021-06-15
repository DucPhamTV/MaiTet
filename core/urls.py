from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from v1.users.urls import user_urlpatterns
from v1.items.urls import router as item_router
from v1.comments.urls import router as comment_router
from v1.addresses.urls import router as address_router
from v2.tracker.urls import router as tracker_router

router = routers.DefaultRouter()
router.registry.extend(item_router.registry)
router.registry.extend(comment_router.registry)
router.registry.extend(address_router.registry)
router.registry.extend(tracker_router.registry)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
] + user_urlpatterns
