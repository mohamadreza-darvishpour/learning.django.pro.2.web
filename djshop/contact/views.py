from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import contact_model_form
from .models import contact_us
# Create your views here.
from .forms import new_glance,direct_model_form
from django.views import View

class contact_profile_view(View):
    def get(self,request):
        return render(request,'contact/contact_prof.html')
    def post(self,request):
        print("\n***************\n",request.FILES,'\n**************')
        return redirect("/co/contact_prof") #return render(request,'contact_prof.html')

from django.views.generic.edit import CreateView
from .models import contact_us
class contact_us4(CreateView ):
    template_name = "contact/contact_us.html"
    # form_class = contact_model_form
    model = contact_us        #it must be modelform
    fields = ['title','message','full_name','email']
    success_url = "/co/contact_us4"
    #when Create view using we can to not define form_valid because it automatically save them.
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)







# from django.views.generic.edit import FormView
# class contact_us4(FormView):
#     template_name = "contact/contact_us.html"
#     form_class = contact_model_form
#     success_url = "/co/contact_us4"
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)






    # def get(self,request):
    #     new_form = direct_model_form()
    #     contact_form = {
    #         "direct_model_forms":new_form,
    #         }
    #     return render(request,"contact/contact_us.html",contact_form)
    # def post(self,request):
    #     contact_form = direct_model_form(request.POST)
    #     if contact_form.is_valid():
    #         contact_form.save()
    #         return redirect(galnce3_contact_page)

def contact_us3(request):
    print("\n************   request.post = ",request.POST,"**********\n")
    if request.method == 'POST':
        new_form = direct_model_form(request.POST)
        if new_form.is_valid():
            print("\n*********  is  valid   *****************\n")
            print("\n@@@@@@@@@@@",new_form.cleaned_data ,"@@@@@@@@\n")
            
            # new_contact =contact_us(
            #     title=  new_form.cleaned_data.get('glance_title') ,
            #     email =  new_form.cleaned_data.get("glance_email")   ,
            #     full_name=  new_form.cleaned_data.get("glance_name")  ,
            #     message=   new_form.cleaned_data.get("glance_text"),  
            # )
            # new_contact.save()
            new_form.save()
        else:
            print("\n*********  isn't valid   *****************\n")
    else:
        print("\n*********  isn't POST   *****************\n")
        new_form = direct_model_form()
    new_contact22 = {
            "direct_model_forms":new_form,
        }
    return render(request,"contact/contact_us.html",new_contact22 )


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

























