from django.shortcuts import render
from .models import Product
from rest_framework import generics, serializers, filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.users.mixins import CustomLoginRequiredMixin
from apps.products.serializers import ProductSerializer
from .models import Product

# Create your views here.

class ProductList(CustomLoginRequiredMixin, generics.ListAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer
    filter_backends= [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields=['category_id', 'type']
    search_fields=['name', 'description']