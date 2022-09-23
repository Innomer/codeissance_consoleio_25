from django.shortcuts import render
from .models import Profile

from django.shortcuts import render,redirect
# Create your views here.
def Login(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    context={}
    if(username and password):
        for prof in Profile.objects.all():
            if(prof.username==username):
                if(prof.pw==password):
                    return redirect('/profile')
                else:
                    context['no_record']=int(0)
            else:
                context['no_record']=int(0)
    return render(request,'LoginSignUp/login.html',context=context)

def Register(request):
    fName=request.POST.get("fullname")
    username=request.POST.get("username")
    password=request.POST.get("password")
    email=request.POST.get("email")
    if(fName and username and password and email):
        prof=Profile()
        prof.username=username
        prof.fullname=fName
        prof.pw=password
        prof.email=email
        prof.save()
        return redirect('/profile')
    return render(request,'LoginSignUp/signUp.html')