from django.db import models

# Create your models here.

Categories= [
    ('PIZZA', 'Pizza'),
    ('BURGER', 'Burger'),
    ('FRENCH FRIES', 'FrenchFries'),
    ('DESERT','Dessert'),
    ('BREVERAGES', 'Breveages'),
    ('BIRYANI', 'Biryani')
]



class FoodItems(models.Model):
    name= models.CharField(max_length=100)
    price= models.IntegerField()
    rating= models.IntegerField()
    food_image = models.ImageField(upload_to='foods/', blank=True, null=True)
    description =models.TextField()
    Categories= models.CharField(max_length=100, choices=Categories)
    

    def __str__(self):
        return self.name

