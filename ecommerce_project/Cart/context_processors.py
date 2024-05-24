from .models import CART, CARTITEM
from .views import cart_id
from django.core.exceptions import ObjectDoesNotExist


def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = CART.objects.filter(cart_id=cart_id(request))
            cart_items = CARTITEM.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity

        except CART.DoesNotExist:
            item_count = 0
        return dict(item_count=item_count)
