from django.contrib import admin

# Register your models here.
from delivery.models import Order
from users.models import CustomUser


class UsersAdmin(admin.ModelAdmin):
    list_display = ('pk','phone' )
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk','deliver','full_name', 'phone','from_address','to_address','landmark', 'created_at')


admin.site.register(Order, OrderAdmin)
admin.site.register(CustomUser, UsersAdmin)