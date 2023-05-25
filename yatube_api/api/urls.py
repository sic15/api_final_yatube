from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    'posts/(?P<post_id>\\d+)/comments',
    CommentViewSet,
    basename='comments')
router.register('follow', FollowViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
