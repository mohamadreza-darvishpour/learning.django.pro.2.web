from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import contact_us_form
# Create your views here.



def contact_us(request):
    #        contact_form = contact_us_form(request.POST or None)

    if request.method == 'POST':
        contact_form = contact_us_form(request.POST)
        if contact_form.is_valid():
            print("*********\n",contact_form.cleaned_data ,"\n*******************")
            return redirect("all_prods")
    else:
        contact_form = contact_us_form()
    contact_form_dict = {
        "contact_form":contact_form,
    }
    return render(request,"contact/contact_us.html",contact_form_dict)