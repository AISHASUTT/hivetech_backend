from django.shortcuts import render, get_object_or_404
from .models import Order

# Create your views here.
def order_items(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    ordered_items = order.orderitem_set.all()

    return render(request, 'orders/order_items.html', {'order': order, 'ordered_items': ordered_items})