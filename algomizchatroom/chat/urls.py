from django.urls import path
from chat import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.registerpage, name='register'),
    path('product/<int:pk>', views.product, name='product'),
    path('deletemessage/<int:pk>', views.deletemessage, name='delete-message'),
    path('userprofile/<int:pk>', views.userprofile, name='userprofile'),
    path('category/', views.categorypage, name='category'),
    path('update_user', views.updateUser, name='update_user'),
    path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
    path('add-cart/<int:id>', views.add_cart, name="add-cart"),
	path('checkout/', views.checkout, name="checkout"),
    ]