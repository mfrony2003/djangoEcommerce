from email import message
from django.http import JsonResponse
from django.shortcuts import redirect, render
from requests import request

from apps.ecommercesite.models import Category, Product
from django.views.generic import TemplateView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
class HomeView(ListView):
    model=Category
    context_object_name='category'
    template_name = 'ecommercesite/home.html' 

class AuthorizeView(LoginRequiredMixin,TemplateView):
    template_name = 'ecommercesite/authorize.html'
    login_url = '/admin/'

@login_required(login_url='/admin/')    
def authorize1(request):
    return render(request, 'ecommercesite/authorize.html')
    

# class ProductbyCategoryView(DetailView):
#   model = Category
#   def get_context_data(self, **kwargs):              
#       products = Product.objects.filter(category_id=request.kwargs['pk'])
#       template_name = 'ecommercesite/ProductbyCategory.html'     
#       context={'products': products}  
#       return context

def ProductbyCategory(request,id):    
    products = Product.objects.filter(category_id=id) 
    context={'products': products}
    return render(request, 'ecommercesite/ProductbyCategory.html', context)

class ProductDetailView(DetailView):   
    model=Product
    context_object_name='product'    
    template_name='ecommercesite/ProductDetailView.html'
    
def categorylistAjax(request):
    category=Category.objects.filter(is_active=True).values("id",'name')
    for i in category:
         i['label']=i.pop('name')
         i['value']=i.pop('id')
    categoryList=list(category)
    return JsonResponse(categoryList, safe=False)

def hellow(request):
    return render(request, 'ecommercesite/hellow.html')

def shoppingcart(request):
    return render(request, 'ecommercesite/shoppingcart.html')



def searchproduct(request):
    if request.method == 'POST':
        searchTerm = request.POST.get('productsearchid')        
        print(searchTerm)
        if searchTerm=="":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product= Product.objects.filter(category_id=searchTerm)
            if product:
                return redirect('ProductbyCategory/'+searchTerm)
            else:
                # message.info(request, 'No product found')
                return redirect(request.META.get('HTTP_REFERER'))
    
    return redirect(request.META.get('HTTP_REFERER'))
            
    
