
from django.urls import path
from apps.ecommercesite import views

urlpatterns = [    
      path('',views.HomeView.as_view(), name='home'),
      path('ProductDetails/<int:pk>',views.ProductDetailView.as_view(), name='ProductDetails'),       
      path('authorize',views.AuthorizeView.as_view(),name='authorize'),            
      path('authorize1',views.authorize1, name='shop'),
      path('ProductbyCategory/<int:id>',views.ProductbyCategory, name='ProductbyCategory'),
      path('categorylistAjax',views.categorylistAjax, name='categorylistAjax'),
      path('searchproduct',views.searchproduct, name='searchproduct'),
      path('hellow',views.hellow, name='hellow'),      
      path('shoppingcart',views.shoppingcart, name='shoppingcart'),
      

      # path('ProductbyCategory/<int:pk>',views.ProductbyCategoryView.as_view(), name='ProductbyCategory'),
]
