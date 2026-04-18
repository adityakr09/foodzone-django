from django.shortcuts import render,redirect
from learningapp.forms import UserForm,UserprofileForm,UserUpdateForm,UserProfileUpdateForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from learningapp.models import UserDetails
from foodsapp.models import FoodItems


# Create your views here.
def registration(request):
    registered = False
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = UserprofileForm(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():  
            user = form1.save() 
            user.set_password(user.password)
            user.save()
            
            profile = form2.save(commit=False)
            profile.user = user         # connecting two models to save the final data
            profile.save()
            registered = True
    else:
        form1 = UserForm()
        form2 = UserprofileForm()
    return render(request, 'registration.html', {'form1': form1,'form2': form2,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return redirect("home")
            else:
                return HttpResponse("user is not active...!!")
        else:
            return HttpResponse("Pls check your creads....")
    return render(request,'login.html')

@login_required(login_url='login')
def home(request):
    allfood = FoodItems.objects.all()
    return render(request,'home.html', {'allfood': allfood})

@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def profile(request):
    userdetails, created = UserDetails.objects.get_or_create(
        user=request.user
    )

    return render(request, 'profile.html', {
        'userdetails': userdetails,
        'user': request.user
    })
    
@login_required(login_url='login')
def update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        form1 = UserProfileUpdateForm(request.POST,request.FILES,instance=request.user.userdetails)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.save()
            profile = form1.save(commit = False)
            profile.user = user
            profile.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
        form1 = UserProfileUpdateForm(instance=request.user.userdetails)
    context = {'form': form,'form1':form1}
    return render(request, 'update.html', context )




