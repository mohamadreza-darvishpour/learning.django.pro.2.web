from django.urls import path
from . import views



urlpatterns = [
    path('all',views.products_show , name='all_prods'),
    path('<prod_slug>',views.product_detail , name= 'prod_detail'),
]
