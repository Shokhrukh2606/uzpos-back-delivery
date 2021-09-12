from django.contrib.auth.models import User, Group
from rest_framework import viewsets, mixins, generics
from rest_framework import permissions

from delivery.models import Order
from delivery.serializers import CustomUserSerializer, GroupSerializer, OrderSerializer
from users.models import CustomUser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = CustomUser.objects.all()
        phone = self.request.query_params.get('phone')
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        if phone is not None:
            queryset = queryset.filter(phone=phone)
        if first_name is not None:
            queryset = queryset.filter(first_name=first_name)
        if last_name is not None:
            queryset = queryset.filter(last_name=last_name)
        return queryset
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]

class OrderAPIView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.UpdateModelMixin,
                      generics.GenericAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)