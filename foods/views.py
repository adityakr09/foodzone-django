from django.shortcuts import render
from foods.models import FoodItems


# Create your views here.
def foodDetail(request,id = 0):
    # take the single food item details based on the id
    fooditem =  FoodItems.objects.get(id = id)
    return render(request,'foods/foodDetails.html',{'fooditem':fooditem})

def allfoods(request):
    category = request.GET.get('category')

    if category:
        allfooditem = FoodItems.objects.filter(Categories=category)
    else:
        allfooditem = FoodItems.objects.all()

    return render(request, 'foods/allfoods.html', {
        'allfooditem': allfooditem,
        'selected_category': category
    })


from django.shortcuts import redirect

def addFood(request):
    if request.method == 'POST':
        FoodItems.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            rating=request.POST.get('rating'),
            Categories=request.POST.get('Categories'),
            description=request.POST.get('description'),
            food_image=request.FILES.get('food_image')
        )
        return redirect('allfoods')

    return render(request, 'foods/addnewfood.html')
