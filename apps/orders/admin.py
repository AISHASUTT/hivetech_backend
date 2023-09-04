from django.contrib import admin


from apps.orders.models import Order

# Register your models here.
@admin.register(Order)
class OrderedModel(admin.ModelAdmin):
    fields=['user', 'customer_name', 'customer_phone', 'address', 'pin_code', 'building_type', 'city','state','total_price', 'total_qty']
    list_display = fields
    list_filter = []
    search_fields=['user']