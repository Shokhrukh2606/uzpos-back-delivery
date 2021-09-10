from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url
from delivery import views

router = DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^orders/$', views.OrderAPIView.as_view()),
    url(r'^orders/(?P<pk>[0-9]+)/$', views.OrderAPIView.as_view()),
    path(r'', include(router.urls)),
]