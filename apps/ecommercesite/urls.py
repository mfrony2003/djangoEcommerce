
from django.urls import path
from apps.ecommercesite import views

urlpatterns = [    
      path('',views.home, name='home'),
      path('shop/<int:id>',views.shop, name='shop'),
      path('details/<int:id>',views.details, name='details'),
]
