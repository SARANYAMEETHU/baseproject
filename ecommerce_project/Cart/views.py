from django.shortcuts import render, redirect, get_object_or_404
from shop.models import PRODUCT
from .models import CART, CARTITEM
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = PRODUCT.objects.get(id=product_id)
    try:
        cart = CART.objects.get(cart_id=cart_id(request))
    except CART.DoesNotExist:
        cart = CART.objects.create(cart_id=cart_id(request))
        cart.save()
    try:
        cart_item = CARTITEM.objects.get(cart=cart, product=product)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
            cart_item.save()
    except CARTITEM.DoesNotExist:
        cart_item = CARTITEM.objects.create(cart=cart, product=product, quantity=1)
        cart_item.save()
    return redirect('Cart:cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = CART.objects.get(cart_id=cart_id(request))
        cart_items = CARTITEM.objects.filter(cart=cart, active=True)
        for cartitem in cart_items:
            total += (cartitem.product.price * cartitem.quantity)
            counter += cartitem.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))


def cart_remove(request, product_id):
    cart = CART.objects.get(cart_id=cart_id(request))
    product = get_object_or_404(PRODUCT, id=product_id)
    cart_item = CARTITEM.objects.get(cart=cart, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('Cart:cart_detail')


def product_remove(request, product_id):
    cart = CART.objects.get(cart_id=cart_id(request))
    product = get_object_or_404(PRODUCT, id=product_id)
    cart_item = CARTITEM.objects.get(cart=cart, product=product)
    cart_item.delete()
    return redirect('Cart:cart_detail')
