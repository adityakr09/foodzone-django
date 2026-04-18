from django.urls import path
from learnapp import views

urlpatterns = [
    path('', views.registration, name='registration'),  # 👈 FIRST PAGE
    path('login/', views.login_view, name='login'),
    path('home', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),  # 👈 NEW PROFILE PATH
    path('update-profile/', views.update_profile, name='update_profile'),
    path ('foods.foodDetails/', views.FoodItems, name= 'foodDetails'),
    path('allfoods/', views.allfoods, name='allfoods'),
]
