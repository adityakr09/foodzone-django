from django.contrib import admin
from .models import FoodItems, SizeOption, BaseOption, ToppingOption, SauceOption

admin.site.register(FoodItems)
admin.site.register(SizeOption)
admin.site.register(BaseOption)
admin.site.register(ToppingOption)
admin.site.register(SauceOption)


