from django.urls import path
from . import views



urlpatterns = [
    path("",views.layout),
    path("inhome",views.index_page),
    #path("contact_us",views.contact_us),
    path("footer_p",views.footer_partial,name="footer_pa"),
    path("header_p",views.header_partial,name="header_pa"),
 
]
