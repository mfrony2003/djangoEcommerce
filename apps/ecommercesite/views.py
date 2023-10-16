from django.shortcuts import render

from apps.ecommercesite.models import Category, Product

def home(request):    
    category = Category.objects.all()    
    context={'category': category}
    return render(request, 'ecommercesite/home.html', context)
def shop(request,id):    
    products = Product.objects.filter(category_id=id) 
    context={'products': products}
    return render(request, 'ecommercesite/shop.html', context)
def details(request,id):    
    product = Product.objects.get(id=id)
    category = Category.objects.all()        
    context={'product': product,'category': category}
    return render(request, 'ecommercesite/detail.html',context )

