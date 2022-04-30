from django.urls import path
from . import views



urlpatterns = [
    path('all',views.products_show),
    path('<int:prod_id>',views.product_detail)
]
