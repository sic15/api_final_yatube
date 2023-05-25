from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import *

app_name = 'api'

router = SimpleRouter()
router.register('v1/posts', PostViewSet)
router.register('v1/groups', GroupViewSet)
router.register(
    'v1/posts/(?P<post_id>\\d+)/comments',
    CommentViewSet,
    basename='comments')
router.register('v1/follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
