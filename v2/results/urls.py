from rest_framework.routers import SimpleRouter

from v2.results.views import ResultViewSet


router = SimpleRouter(trailing_slash=False)
router.register('result', ResultViewSet)
