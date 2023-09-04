from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    fields = ['name', 'description', 'price', 'type', 'image', 'category']
    list_display = fields
    list_filter = []
    search_fields = ['name', 'description']
    
