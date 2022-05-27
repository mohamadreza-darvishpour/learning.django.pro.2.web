from django.shortcuts import render

# Create your views here.



def contact_us(request):
    if request.method =='POST':
        print(request.POST)
    return render(request,"contact/contact_us.html",{})