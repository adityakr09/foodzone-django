from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from learnapp.forms import UserForm, UserProfile
from learnapp.models import UserDetails
from foods.models import FoodItems



from django.contrib import messages



def registration(request):
    registered = False

    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = UserProfile(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = form2.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
    else:
        form1 = UserForm()
        form2 = UserProfile()

    return render(request, 'registration.html', {
        'form1': form1,
        'form2': form2,
        'registered': registered
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("User is not active.")
        else:
            return HttpResponse("Please check your credentials.")

    return render(request, 'login.html')


@login_required(login_url='login')
def home(request):
    allfoods = FoodItems.objects.all()
    return render(request, 'home.html', {'allfoods': allfoods})

def allfoods(request):
    return render(request, 'foods/allfoods.html')




@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    userdetails, created = UserDetails.objects.get_or_create(
        user=request.user
    )

    return render(request, 'profile.html', {
        'userdetails': userdetails,
        'user': request.user
    })





@login_required
def update_profile(request):
    0
    user = request.user
    userdetails = UserDetails.objects.get(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfile(
            request.POST,
            request.FILES,
            instance=userdetails
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfile(instance=userdetails)

    return render(request, 'update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



