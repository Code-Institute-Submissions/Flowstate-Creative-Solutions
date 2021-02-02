from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    discount = 0
    discount_code = settings.DISCOUNT_CODE
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += product.price
        product_count = quantity
        cart_items.append({
            'item_id': item_id,
            'product': product,
        })
    
    # need to add discount code algorythm here and adjust grand_total
    # if discount_code in request.POST?

    

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'discount': discount,
        'grand_total': grand_total,
        'discount_code': discount_code,
    }

    return context