from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import contact_us_form
from .models import contact_us
# Create your views here.



def contact_us2(request):
    #        contact_form = contact_us_form(request.POST or None)

    if request.method == 'POST':
        contact_form = contact_us_form(request.POST)
        if contact_form.is_valid():
            print("*********\n",contact_form.cleaned_data ,"\n*******************")
            new_contact = contact_us(
                email=contact_form.cleaned_data.get('email'),
                title=contact_form.cleaned_data.get('subject'),
                full_name=contact_form.cleaned_data.get('full_name'),
                message=contact_form.cleaned_data.get('text'),
                is_read_by_admin=False,
            )
            new_contact.save()

            
            
            return redirect("all_prods")
    else:
        contact_form = contact_us_form()
    contact_form_dict = {
        "contact_form":contact_form,
    }
    return render(request,"contact/contact_us.html",contact_form_dict)