from rest_framework.routers import SimpleRouter

from v1.comments.views import CommentViewSet

router = SimpleRouter(trailing_slash=False)
router.register('comments', CommentViewSet)
