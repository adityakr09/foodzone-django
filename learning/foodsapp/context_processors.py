from .models import Cart

def cart_item_count(request):
    count = 0
    if request.user.is_authenticated:
        count = Cart.objects.count()
    return {"cart_count": count}

