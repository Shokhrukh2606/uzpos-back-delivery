from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from delivery import views

router = DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
urlpatterns = [
    path(r'', include(router.urls)),
]