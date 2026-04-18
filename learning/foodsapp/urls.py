from django.urls import path
from . import views

app_name = "foodsapp"

urlpatterns = [
    path('allfoods/', views.allfoods, name='allfoods'),
    path('food/<int:id>/', views.Food_details, name='food_details'),
    path("food/<int:id>/customize/", views.customizeFood, name="customizeFood"),
    path("add-to-cart/<int:id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart_view, name="cart"),
    path("remove-cart/<int:id>/", views.remove_cart, name="remove_cart"),
    path("increase-qty/<int:id>/", views.increase_qty, name="increase_qty"),
    path("decrease-qty/<int:id>/", views.decrease_qty, name="decrease_qty"),
    path("make-order/", views.make_order, name="make-order"),
    path("order-success/<uuid:order_id>/", views.order_success, name="order_success"),
    path("billing/<uuid:order_id>/",views.billing_view,name="billing"),
    path("proceed-payment/<uuid:order_id>/",views.proceed_to_payment,name="proceed_payment"),
]
