from django.db import models

# Create your models here.

class FoodItems(models.Model):
    Catageries = [
        ("PIZZA","Pizza"),
        ("BURGER","Burger"),
        ("FRENCH FRIES","French Fries"),
        ("DESSARTS","Dessarts"),
        ("BREVERAGES","Breverages"),
        ("BRIYANI","Briyani")
    ]
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.IntegerField()
    foodimg = models.ImageField(upload_to = "foodimg/",blank=True,null = True)
    description = models.TextField()
    catogery = models.CharField(max_length=100,choices=Catageries)
    
    def __str__(self):
        return self.name


class SizeOption(models.Model):
    food = models.ForeignKey(FoodItems, on_delete=models.CASCADE, related_name="sizes")
    category = models.CharField(max_length=100, choices=FoodItems.Catageries)
    size = models.CharField(max_length=50) 
    size_cm = models.DecimalField(max_digits=5, decimal_places=1)  
    extra_price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="cuimg/", blank=True, null=True)

    def __str__(self):
        return f"{self.food.name} - {self.size} ({self.size_cm} cm)"


class BaseOption(models.Model):
    food = models.ForeignKey(FoodItems, on_delete=models.CASCADE, related_name="bases")
    category = models.CharField(max_length=100, choices=FoodItems.Catageries)
    basetype = models.CharField(max_length=50)  # Thin Crust / Thick Crust
    extra_price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="cuimg/", blank=True, null=True)

    def __str__(self):
        return f"{self.food.name} - {self.basetype}"

class ToppingOption(models.Model):
    food = models.ForeignKey(FoodItems, on_delete=models.CASCADE, related_name="toppings")
    category = models.CharField(max_length=100, choices=FoodItems.Catageries)
    toppingname = models.CharField(max_length=80)
    extra_price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="cuimg/", blank=True, null=True)

    def __str__(self):
        return f"{self.food.name} - {self.toppingname}"

class SauceOption(models.Model):
    food = models.ForeignKey(FoodItems, on_delete=models.CASCADE, related_name="sauces")
    category = models.CharField(max_length=100, choices=FoodItems.Catageries)
    sausetype = models.CharField(max_length=80) 
    extra_price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="cuimg/", blank=True, null=True)

    def __str__(self):
        return f"{self.food.name} - {self.sausetype}"


class CustomizedOption(models.Model):
    OPTION_TYPES = [
        ("SIZE", "Size"),
        ("BASE", "Base"),
        ("TOPPING", "Topping"),
        ("SAUCE", "Sauce"),
    ]

    food = models.ForeignKey(FoodItems, on_delete=models.CASCADE, related_name="custom_options")
    category = models.CharField(max_length=100, choices=FoodItems.Catageries)

    option_type = models.CharField(max_length=10, choices=OPTION_TYPES)
    name = models.CharField(max_length=100)

    size_cm = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)  # only for SIZE
    extra_price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="cuimg/", blank=True, null=True)

    def save(self, *args, **kwargs):
        self.category = self.food.catogery
        super().save(*args, **kwargs)

    def __str__(self):
        if self.option_type == "SIZE" and self.size_cm is not None:
            return f"{self.food.name} - {self.name} ({self.size_cm} cm)"
        return f"{self.food.name} - {self.name}"


class Customization(models.Model):
    food = models.ForeignKey(FoodItems, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Customization #{self.id} - {self.food.name}"


class CustomizationItem(models.Model):
    customization = models.ForeignKey(Customization, on_delete=models.CASCADE, related_name="items")
    option = models.ForeignKey(CustomizedOption, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customization.food.name} - {self.option.option_type} - {self.option.name}"


class Cart(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.IntegerField()
    foodimg = models.ImageField(upload_to="foodimg/", blank=True, null=True)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name


import uuid
from django.contrib.auth.models import User

class Order(models.Model):
    order_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Delivered", "Delivered"),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

    def __str__(self):
        return str(self.order_id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    food_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.food_name
