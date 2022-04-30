from django.shortcuts import render
from .models import products
# Create your views here.


def products_show(request):
    prod_dict ={
        'all_products':products.objects.all(),
    }
    return render(request,'products/products_list.html',prod_dict)

from django.http import Http404
def product_detail(request,prod_id):
    '''
    try:
        prods=products.objects.get(id=prod_id)
    except:
        raise Http404("this isn't found")
    ''' 
    from django.shortcuts import get_object_or_404
    prods=get_object_or_404(products,id=prod_id)
    detail_dict = {
        'a_product':prods,
    }
    return render(request,'products/item_detail.html',detail_dict)



    