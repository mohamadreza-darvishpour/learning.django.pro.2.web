from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import contact_model_form
from .models import contact_us
# Create your views here.
from .forms import new_glance,direct_model_form

def contact_us3(request):
    if request.POST== 'POST':
        new_form = direct_model_form(request.POST)
        if new_form.is_valid():
            print("\n@@@@@@@@@@@",new_form.cleaned_data ,"@@@@@@@@\n")
            new_contact =contact_us(
                title=  new_form.cleaned_data.get('glance_title') ,
                email =  new_form.cleaned_data.get("glance_email")   ,
                full_name=  new_form.cleaned_data.get("glance_name")  ,
                message=   new_form.cleaned_data.get("glance_text"),  
            )
            new_contact.save()
    else:
        new_form = new_glance()
    new_contact = {
            "direct_model_form":new_form,
        }
    return render(request,"contact/contact_us.html",new_contact )


def contact_us1(request):
    if request.POST== 'POST':
        new_form = new_glance(request.POST)
        if new_form.is_valid():
            print("\n@@@@@@@@@@@",new_form.cleaned_data ,"@@@@@@@@\n")
            new_contact =contact_us(
                title=  new_form.cleaned_data.get('glance_title') ,
                email =  new_form.cleaned_data.get("glance_email")   ,
                full_name=  new_form.cleaned_data.get("glance_name")  ,
                message=   new_form.cleaned_data.get("glance_text"),  
            )
            new_contact.save()
    else:
        new_form = new_glance()
    new_contact = {
            "new_form_dic":new_form,
        }
    return render(request,"contact/contact_us.html",new_contact )

def contact_us2(request):
    #        contact_form = contact_model_form(request.POST or None)

    if request.method == 'POST':
        contact_form = contact_model_form(request.POST)
        if contact_form.is_valid():
            print("*********\n",contact_form.cleaned_data ,"\n*******************")
            new_contact = contact_us(
                email=contact_form.cleaned_data.get('email'),
                title=contact_form.cleaned_data.get('title'),
                full_name=contact_form.cleaned_data.get('full_name'),
                message=contact_form.cleaned_data.get('message'),
            
            )
            new_contact.save()

            
            
            return redirect("all_prods")
    else:
        contact_form = contact_model_form()
    contact_form_dict = {
        "contact_form":contact_form,
    }
    return render(request,"contact/contact_us.html",contact_form_dict)

























