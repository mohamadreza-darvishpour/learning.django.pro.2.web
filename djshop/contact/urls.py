from django.urls import path
from . import views
urlpatterns = [
    path("contact_us4",views.contact_us4.as_view(),name="class4_contact_page"),
    path("contact_us3",views.contact_us3,name="glance3_contact_page"),
    path("contact_us1",views.contact_us1,name="glance_contact_page"),
    path("contact_us",views.contact_us2,name="contact_page"),
]
