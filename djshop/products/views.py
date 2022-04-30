from django.shortcuts import render
from .models import products
# Create your views here.


def products_show(request):
    prod_dict ={
        'all_products':products.objects.all(),
    }
    return render(request,'products/products_list.html',prod_dict)




    