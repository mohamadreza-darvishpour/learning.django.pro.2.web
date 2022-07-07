from django.shortcuts import render

# Create your views here.

from django.views import View
# class index_page_view(View):
#     def get(self,request):
#         context ={
#             "data":"given data..."
#         }
#         return render(request,"home_module/index_page1.html",context)


from django.views.generic.base import TemplateView
class index_page_view(TemplateView):
    template_name = "home_module/index_page1.html"
    #how to send data by TemplateView
    def get_context_data(self,**kwargs):
        new_data = super().get_context_data(**kwargs)
        #if you do not need any additional data return"super().get_context_data(**kwargs)" if not make it in variable and use it in a way below.
        new_data["data32"] = "given data 32"
        return new_data
        


# def index_page(request):
#     return render(request,'home_module/index_page1.html')


def header_partial(request):
    return render(request,"shared/header_partial.html")

def footer_partial(request):
    return render(request,"shared/footer_partial.html")

def contact_us(request):
    return render(request,"contact_us")

def layout(request):
    return render(request,"_layout.html")