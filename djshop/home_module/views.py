from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request,'home_module/index_page1.html')


def header_partial(request):
    return render(request,"shared/header_partial.html")

def footer_partial(request):
    return render(request,"shared/footer_partial.html")

def contact_us(request):
    return render(request,"contact_us")

def layout(request):
    return render(request,"_layout.html")