from django.shortcuts import render
from .models import Profile
from random import randint
from django.shortcuts import render,redirect
# Create your views here.
token=0

def Login(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    context={}
    if(username and password):
        for prof in Profile.objects.all():
            if(prof.username==username):
                if(prof.pw==password):
                    request.session['token']=prof.token
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
    context={}
    if(fName and username and password and email):
        prof=Profile()
        prof.username=username
        prof.fullname=fName
        prof.pw=password
        prof.email=email
        x=randint(10000000,99999999)
        prof.token=x
        prof.save()
        request.session['token']=x
        return redirect('/profile')
    else:
        context['no_record']=int(0)
    return render(request,'LoginSignUp/signUp.html',context=context)