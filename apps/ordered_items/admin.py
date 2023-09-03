from django.contrib import admin
from apps.orders.models import Product

# Register your models here.
class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'paid')
    list_filter = ('paid',)
    inlines = [OrderItemInLine]