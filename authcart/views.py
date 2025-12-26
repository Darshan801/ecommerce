from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def sign_up(request):
    if(request.method=='POST'):
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password != confirm_password:
            # messages.warning(request,"password dont match")
            return HttpResponse("password dont match")
            # return render(request,'auth/signup.html')
        try:
            if User.objects.get(username=email):
                return HttpResponse("email already exitsts")
                # messages.warning(request,"email is taken")
                # return render(request,'auth/signup.html')
        except User.DoesNotExist:
            pass
        user=User.objects.create_user(username=email , email=email , password=password)
        user.save()
        return HttpResponse('user created',email)
    return render(request,'authentication/signup.html')

def handlelogin(request):
    return render(request,'authentication/login.html')

def handlelogout(request):
    return redirect('/auth/login')

