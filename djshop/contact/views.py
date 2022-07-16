from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import contact_model_form,profile_form
from .models import contact_us,profile_images
# Create your views here.
from .forms import new_glance,direct_model_form
from django.views import View


#how to save or store uploaded files
def save_file(file):
    with open("temp/uploaded_pic.jpg","wb+")as dest:
        for chunk in file.chunks():
            dest.write(chunk)


#use createview to get profile pic.
from django.views.generic.edit import CreateView
class contact_profile_view(CreateView):
    template_name = 'contact/contact_prof.html'
    model = profile_images
    fields = '__all__'
    success_url = "contact_prof"#reverse('contact_profile')
    context_object_name = "form"

from django.views.generic.list import ListView 
from .models import profile_images
class profiles_list(ListView):
    template_name = 'contact/profiles_list.html'
    model = profile_images
    context_object_name = "images"
    

# class contact_profile_view(View):
#     def get(self,request):
#         image_form = profile_form()
#         form = {"form":image_form,}
#         return render(request,'contact/contact_prof.html',form)
#     def post(self,request):
#         model_variable = profile_images(image= request.FILES['image_form'])
#         model_variable.save()
#         return redirect("/co/contact_prof") #return render(request,'contact_prof.html')






# class contact_profile_view(View):
#     def get(self,request):
#         image_form = profile_form()
#         form = {"form":image_form,}
#         return render(request,'contact/contact_prof.html',form)
#     def post(self,request):
#         submitted_form = profile_form(request.POST ,request.FILES )
#         if submitted_form.is_valid:
#             save_file(request.FILES['image_form'])
#             return redirect("class4_contact_page")
#         return redirect("/contact_prof") #return render(request,'contact_prof.html')







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

























