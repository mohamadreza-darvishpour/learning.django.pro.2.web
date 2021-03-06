from django.shortcuts import render
from .models import products
from django.views.generic.base import TemplateView
# Create your views here.
from django.shortcuts import redirect

#a class to use session and save info in sessions 
from django.views import View
class favorite_product_view(View):
    def post(self,request):
        favorite_prod_id = request.POST['favorite_prod_id']
        product = products.objects.get(id=favorite_prod_id)
        request.session["favorite_product"] = str(favorite_prod_id)
        return redirect(product.get_absolute_url())




#another way to show list of datas in db
from django.views.generic import ListView
class product_show_view(ListView):
    template_name = "products/shop.html"
    model = products
    context_object_name = "all_products" #name sends data to html through
    #notice: if 'context_object_name' didn't defined django automatically send by default name ="object_list"
    
    def get_queryset(self):
        query1 =  super(product_show_view,self).get_queryset()
        filtered_data = query1.filter(price__lt=1087)
        return filtered_data
    

#a way to get and show from db
# from django.views.generic.base import TemplateView
# class product_show_view(TemplateView):
#     template_name = "products/shop.html"
#     def get_context_data(self, **kwargs):
#         db_data = products.objects.all().order_by('-price')
#         context = super().get_context_data(**kwargs)
#         context["all_products"] = db_data
#         return context
    

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
class product_detail_view(DetailView):
    template_name = "products/item_detail.html"
    model = products
    #context_object_name = "products_list"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        product_loaded = self.object.id
        request = self.request
        #favorite_prod_id_in_session = request.session['favorite_product']
        favorite_prod_id_in_session = request.session.get('favorite_product')
        context["is_favorite"] = str(favorite_prod_id_in_session)==str(product_loaded)
        return context



# class product_detail_view(TemplateView):
#     template_name = "products/item_detail.html"
    
#     def get_context_data(self,**kwargs):
#         given_data = super(product_detail_view,self).get_context_data()
#         slug = kwargs["prod_slug"]
#         db_data = get_object_or_404(products,slug=slug)
#         given_data["a_product"] = db_data
#         return given_data

# def products_show(request):
#     prods = products.objects.all().order_by('price')
#     #count the products.
#     number_of_products = prods.count()
#     #count avg of raitngs
#     from django.db.models import Avg,Min
#     #rating_features = prods.aggregate(Avg("rating"),Min("rating"))
#     prod_dict ={
#         'all_products':prods,
#         #'fitures_rating':rating_features,
#         'total_number':number_of_products,
#     }
#     return render(request,'products/shop.html',prod_dict)




# from django.http import Http404 
# def product_detail(request,prod_slug):
#     from django.shortcuts import get_object_or_404
#     pr_slug = get_object_or_404(products,slug=prod_slug)
#     detail_dict = {
#         'a_product':pr_slug,
#     }
#     return render(request,'products/item_detail.html',detail_dict)
   

    