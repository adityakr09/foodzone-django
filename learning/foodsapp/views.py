from django.shortcuts import render, get_object_or_404, redirect
from .models import FoodItems, BaseOption, SizeOption, ToppingOption, SauceOption,Cart,Order, OrderItem
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from foodsapp.utils import send_email_view




def allfoods(request):
    selected_category = request.GET.get("catogery")
    foods = FoodItems.objects.all()
    if selected_category:
        foods = foods.filter(catogery=selected_category)

    return render(request, "foods/allfoods.html", {
        "allfooditem": foods,
        "categories": FoodItems.Catageries,
        "selected_category": selected_category,
    })


def Food_details(request, id):
    food = get_object_or_404(FoodItems, id=id)
    return render(request, "foods/foodDetails.html", {"fooditems": food})


def customizeFood(request, id):
    food = get_object_or_404(FoodItems, id=id)

    context = {
        "food": food,
        "base_options": BaseOption.objects.filter(food=food),
        "size_options": SizeOption.objects.filter(food=food),
        "topping_options": ToppingOption.objects.filter(food=food),
        "sauce_options": SauceOption.objects.filter(food=food),
    }

    if request.method == "POST":
        return redirect("foodsapp:food_details", id=food.id)

    return render(request, "foods/customize.html", context)


def addFood(request):
    if request.method == "POST":
        FoodItems.objects.create(
            name=request.POST.get("name"),
            price=request.POST.get("price") or 0,
            rating=request.POST.get("rating") or 0,
            catogery=request.POST.get("catogery"),
            description=request.POST.get("description"),
            foodimg=request.FILES.get("foodimg"),
        )
        return redirect("foodsapp:allfoods")

    return render(request, "foods/addnewfood.html")

def add_to_cart(request, id):
    food = get_object_or_404(FoodItems, id=id)

    cart_item, created = Cart.objects.get_or_create(
        name=food.name,
        defaults={
            "price": food.price,
            "rating": food.rating,
            "foodimg": food.foodimg,
            "description": food.description,
            "quantity": 1
        }
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("foodsapp:cart")



def cart_view(request):
    cart_items = Cart.objects.all()

    total_price = sum(item.price * item.quantity for item in cart_items)

    return render(request, "cart.html", {
        "cart_items": cart_items,
        "total_price": total_price
    })
    
    
def increase_qty(request, id):
    item = get_object_or_404(Cart, id=id)
    item.quantity += 1
    item.save()
    return redirect("foodsapp:cart")


def decrease_qty(request, id):
    item = get_object_or_404(Cart, id=id)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect("foodsapp:cart")


def remove_cart(request, id):
    item = get_object_or_404(Cart, id=id)
    item.delete()
    return redirect("foodsapp:cart")


@login_required
def make_order(request):

    cart_items = Cart.objects.all()

    if not cart_items.exists():
        return redirect("foodsapp:cart")

    total_price = sum(item.price * item.quantity for item in cart_items)

    # Create Order
    order = Order.objects.create(
        user=request.user,
        total_price=Decimal(total_price),
        status="Pending"
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            food_name=item.name,
            quantity=item.quantity,
            price=item.price
        )

    return redirect("foodsapp:order_success", order_id=order.order_id)


@login_required
def proceed_to_payment(request, order_id):

    order = Order.objects.get(order_id=order_id)

    address = "Home Delivery Address"   

   
    order.status = "Confirmed"
    order.save()

    
    Cart.objects.all().delete()

 
    send_email_view(
        email=request.user.email,
        user=request.user,
        order=order,
        address=address,
    )

    return redirect("foodsapp:billing", order_id=order.order_id)



def order_success(request, order_id):
    order = Order.objects.get(order_id=order_id)
    return render(request, "foods/order_success.html", {"order": order})



@login_required
def billing_view(request, order_id):
    order = get_object_or_404(Order, order_id=order_id, user=request.user)

    items = OrderItem.objects.filter(order=order)

    total_qty = sum(item.quantity for item in items)

    context = {
        "order": order,
        "items": items,
        "total_qty": total_qty,
    }

    return render(request, "foods/billing.html", context)






