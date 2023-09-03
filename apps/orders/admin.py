from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

class OrderItemInLine(admin.ModelAdmin):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'creatted_at', 'paid')
    list_filter = ('paid',)
    inlines = [OrderItemInLine]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')