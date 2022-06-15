from django.urls import path
from . import views
urlpatterns = [
    path("contact_us",views.contact_us2,name="contact_page"),
]
