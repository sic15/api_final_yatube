from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api import views

app_name = 'api'

router = SimpleRouter()
router.register('v1/posts', views.PostViewSet)
router.register('v1/groups', views.GroupViewSet)
router.register(
    'v1/posts/(?P<post_id>\\d+)/comments',
    views.CommentViewSet,
    basename='comments')
router.register('v1/follow', views.FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
