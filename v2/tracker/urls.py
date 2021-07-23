from rest_framework.routers import SimpleRouter

from v2.tracker.views import TrackerViewSet


router = SimpleRouter(trailing_slash=False)
router.register('tracker', TrackerViewSet)
