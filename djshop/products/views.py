from django.shortcuts import render
from .models import products
# Create your views here.


def products_show(request):
    prods = products.objects.all().order_by('price')
    #count the products.
    number_of_products = prods.count()
    #count avg of raitngs
    from django.db.models import Avg,Min
    #rating_features = prods.aggregate(Avg("rating"),Min("rating"))
    prod_dict ={
        'all_products':prods,
        #'fitures_rating':rating_features,
        'total_number':number_of_products,
    }
    return render(request,'products/shop.html',prod_dict)

from django.http import Http404
def product_detail(request,prod_slug):
    '''
    try:
        prods=products.objects.get(id=prod_id)
    except:
        raise Http404("this isn't found")
    ''' 
    list_slug = prod_slug.split("_")
    prod_id = int(list_slug[0])
    from django.shortcuts import get_object_or_404
    prods = get_object_or_404(products,id=prod_id)
   
    detail_dict = {
        'a_product':prods,
    }
    return render(request,'products/item_detail.html',detail_dict)



    