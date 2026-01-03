from django.shortcuts import render
from django.http import HttpResponse
from core.models import Contact,Product
from django.contrib import messages
from math import ceil

# Create your views here.
def index(request):
    allproducts=[]
    catprods=Product.objects.values('category','id')
    # print(catprods)
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat) #to filter based on category
        n=len(prod)
        nslides=n//4 + ceil((n/4)-(n//4))
        allproducts.append([prod, range(1, nslides + 1), nslides])
    params={'allproducts':allproducts}
    return render(request,'core/index.html',params)

def contact(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname','')
        email=request.POST.get('email','')
        desc=request.POST.get('desc','')
        phone=request.POST.get('phone','')
        #phone validation
        if not phone or not phone.isdigit() or len(phone) != 10:
            messages.error(request,"Phone number must be exactly 10 digits")
            return render(request,'core/contact.html',{
                'fullname':fullname,
                'email':email,
                'desc':desc,
                'phone':phone
            })
        myquery=Contact(name=fullname , email=email , desc=desc , phonenumber=phone)
        myquery.save()
        messages.warning(request,"We will get back soon")
        return render(request,'core/contact.html')
    return render(request,'core/contact.html')

def about(request):
    return render(request,'core/about.html')

def sign_in(request):
    return render(request,'core/signin.html')