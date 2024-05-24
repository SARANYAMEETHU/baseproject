from . import views
from django.urls import path

app_name = 'Cart'
urlpatterns = [
        path('add/<int:product_id>', views.add_cart,name="add_cart"),
        path('cart/', views.cart_detail, name='cart_detail'),
        path('remove/<int:product_id>/', views.cart_remove, name="cart_remove"),
        path('product_remove/<int:product_id>/', views.product_remove, name="product_remove"),

]
