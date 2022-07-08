from django.urls import path
from . import views



urlpatterns = [
    path('all',views.product_show_view.as_view() , name='all_prods'),
    path('<slug:prod_slug>',views.product_detail_view.as_view() , name= 'prod_detail'),
]
