
from django.contrib import admin
from django.urls import path
from .import views as v
urlpatterns = [
    path('getcategory/<int:id>/', v.get_by_category ,name='get_by_category'),
    path('search',v.search_product,name='search'),
    path('register',v.addUser,name='regist'),
    path('login',v.login_view,name='login'),
    path('logout',v.logout_view,name='logout'),
    path('addcart/<int:id>/',v.addtocart,name='addToCart'),
    path('cart',v.cart_list,name='crlist'),
    path('order',v.my_order,name='morder'),
]
