from django.contrib import admin
from chat.models import Message, Category, User, Customer, Cart, Product, Order, OrderItem 
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Message)
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)