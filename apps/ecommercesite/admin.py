from django.contrib import admin

from apps.ecommercesite.models import Category, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)