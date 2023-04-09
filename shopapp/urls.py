from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
      path('',views.index,name="home"),
      path('login',views.login_page,name="login"),
      path('signup',views.signup,name="signup"),
      path('addcart',views.add_to_cart,name="addcart"),
      path('logout',views.logout_page,name="logout]"),
      path('category',views.category,name="category"),
      path('category/<str:name>',views.categoryview,name="category"),
      path('category/<str:cname>/<str:pname>',views.product_details,name="product_details"),
      path('cart',views.cart_page,name="cart"),
      path('remove_cart/<str:cid>',views.remove_cart ,name="remove_cart")
    
      
]
