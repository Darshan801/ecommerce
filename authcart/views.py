from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from .utils import generate_token, TokenGenerator
from django.utils.encoding import force_bytes , force_str , DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate , login , logout
import re
# Create your views here.
def sign_up(request):
    if(request.method=='POST'):
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        #password validation
        if(
            len(password) < 8 or 
            not re.search(r"[A-Za-z]",password) or
            not re.search(r"[0-9]",password) or
            not re.search(r"[!@#$%^&*(),.?\":{}|<>]",password)
        ):
            messages.warning(request,"Password must be at least 8 characters long and contain a letter, a number, and a special character")
            return render(request,'authentication/signup.html')
        # password match check
        if password != confirm_password:
            messages.warning(request,"password don't  match")
            # return HttpResponse("password dont match")
            return render(request,'authentication/signup.html')
        try:
            if User.objects.get(username=email):
                # return HttpResponse("email already exitsts")
                messages.warning(request,"email is taken")
                return render(request,'authentication/signup.html')
        except User.DoesNotExist:
            pass
        user=User.objects.create_user(username=email , email=email , password=password)
        user.is_active=False
        user.save()
        email_subject="activate your account"
        message=render_to_string('authentication/activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
        })

#         send_mail(
#     "Subject here",
#     "Here is the message.",
#     "from@example.com",
#     ["to@example.com"],
#     fail_silently=False,
# )
        email_message = EmailMessage(email_subject , message , settings.EMAIL_HOST_USER,[email],)
        email_message.send()
        messages.success(request,"Activate your account by clicing the link in your gmail")
        return redirect('/auth/login/')

    return render(request,'authentication/signup.html')



class ActivateAccountView(View):
    def get(self, request , uidb64 , token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"account activated ")
            return redirect('/auth/login')
        return render(request,'activatefail.html')

    


def handlelogin(request):
    if(request.method=='POST'):
        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username, password=userpassword)
        
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"login success")
            # return render(request,'core/index.html') 
            return redirect('/')
        else:
            messages.error(request,"invalid credentials")
            return redirect('/auth/login')
    return render(request,'authentication/login.html')

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout success")
    return redirect('/auth/login')

