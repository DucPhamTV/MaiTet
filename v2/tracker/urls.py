from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from v2.tracker.views import TrackerViewSet
from v2.results.views import ResultViewSet


router = SimpleRouter(trailing_slash=False)
router.register('tracker', TrackerViewSet)

tracker_nested_router = routers.NestedSimpleRouter(
    router, 'tracker', lookup='tracker')
tracker_nested_router.register(
    'results', ResultViewSet, basename='tracker-results')
#urlpatterns = patterns('',
#    url(r'^', include(router.urls)),
#    url(r'^', include(tracker_nested_router.urls)),
#)
