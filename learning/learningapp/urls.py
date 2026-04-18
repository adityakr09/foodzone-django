from django.urls import path
from learningapp import views


urlpatterns = [
    path('',views.registration,name="register"),
    path('login/',views.user_login,name="login"),
    path('home',views.home,name="home"),
    path('logout',views.user_logout,name="logout"),
    path('profile',views.profile,name="profile"),
    path('update',views.update,name='update'),
    path('foodsapp.foodDetails',views.FoodItems,name="foodDetails"),
    # path('allfoods',views.allfoods,name='allfoods'),
    
]
