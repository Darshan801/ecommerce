from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def sign_up(request):
    return render(request,'authentication/signup.html')

def handlelogin(request):
    return render(request,'authentication/login.html')

def handlelogout(request):
    return redirect('/authcart/login')

