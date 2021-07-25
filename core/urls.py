from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from v1.items.urls import router as item_router
from v1.comments.urls import router as comment_router
from v1.addresses.urls import router as address_router
from v2.tracker.urls import router as tracker_router, tracker_nested_router
from v2.results.urls import router as result_router

router = routers.DefaultRouter()
router.registry.extend(item_router.registry)
router.registry.extend(comment_router.registry)
router.registry.extend(address_router.registry)


# Wire up our API using automatic URL routing.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('', include(router.urls)),
        path('auth/', include('djoser.urls')),
        path('auth/', include("djoser.urls.authtoken")),
        path('', include(tracker_router.urls)),
        path('', include(tracker_nested_router.urls)),
    ])),
]

