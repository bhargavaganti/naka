from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from projects.views import ProjectViewSet, TagListViewSet
from users.views import UserCreateViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tags', TagListViewSet)
router.register(r'users', UserCreateViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^auth/', include('naka.auth_urls')),
]
