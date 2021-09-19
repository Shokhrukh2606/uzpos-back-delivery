from django.contrib.auth.models import Group
from rest_framework import serializers

from delivery.models import Order, OrderItem, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ['phone', 'pk', 'groups', 'first_name', 'last_name', 'date_joined', 'last_login', 'password',
                  'is_active']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product_id', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, required=True)

    def create(self, validated_data):
        items = validated_data.pop('items', [])
        instance = Order.objects.create(**validated_data)
        for item in items:
            saved_item = OrderItem.objects.create(**item, order_id=instance)
            instance.items.add(saved_item)
        return instance

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', {})
        items_serializer = OrderItemSerializer(instance.items, data=items_data)
        if items_serializer.is_valid():
            items_serializer.save()
        return instance

    class Meta:
        model = Order
        fields = ['pk', 'full_name', 'phone', 'from_address', 'to_address', 'landmark', 'items']
