from django.urls import path
from . import views



urlpatterns = [
    path("inhome",views.index_page),

]
