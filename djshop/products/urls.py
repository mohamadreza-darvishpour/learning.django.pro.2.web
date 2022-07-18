from django.urls import path
from . import views



urlpatterns = [
    path('all',views.product_show_view.as_view() , name='all_prods'),
    path("favorite_product",views.favorite_product_view.as_view(),name="favorite_prod_url"),
    path('<slug:slug>',views.product_detail_view.as_view() , name= 'prod_detail'),
]
