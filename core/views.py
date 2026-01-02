from django.shortcuts import render
from django.http import HttpResponse
from core.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def contact(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        phone=request.POST.get('phone')
        myquery=Contact(name=fullname , email=email , desc=desc , phonenumber=phone)
        myquery.save()
        messages.warning(request,"We will get back soon")
        return render(request,'core/contact.html')
    return render(request,'core/contact.html')

def about(request):
    return render(request,'core/about.html')

def sign_in(request):
    return render(request,'core/signin.html')