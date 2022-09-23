from django.shortcuts import render
from .models import Profile
from random import randint
from django.shortcuts import render,redirect
import json
# Create your views here.

from django.forms.models import model_to_dict
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
                    context['username']=username
                    context['pw']=password
                    return redirect("/profile/{}".format(int(prof.token)))
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
        return redirect('/profile/{}'.format(x))
    else:
        context['no_record']=int(0)
    return render(request,'LoginSignUp/signUp.html',context=context)

def Prof(request,id):
    if id > 10000000:
        prof=Profile.objects.filter(token=id).first()
        info={'1':1}
        if(prof):
            info=model_to_dict(prof)
        abt=request.POST.get("About")
        username=request.POST.get("Username")
        fName=request.POST.get("fname")
        ed=request.POST.get("Edu")
        dt=request.POST.get("Date")
        city=request.POST.get("City")
        country=request.POST.get("Country")
        career=request.POST.get("Career")
        interests=request.POST.get("Interest")
        pp=request.POST.get("img")
        i1=request.POST.get("Interest1")
        i2=request.POST.get("Interest2")
        i3=request.POST.get("Interest3")
        c1=request.POST.get("Community1")
        c2=request.POST.get("Community2")
        c3=request.POST.get("Community3")
        if dt:
            if pp:
                pp='/'+pp
            if interests:
                interests=enumerate(interests,1)
            community=request.POST.get("Community")
            if community:
                community=enumerate(community,1)
            if id:
                p=Profile.objects.filter(token=id).get()
                p.username=username
                p.fullname=fName
                p.ed=ed
                p.abt=abt
                p.bday=dt
                p.city=city
                p.country=country
                p.career=career
                p.interest=interests
                p.communities=community
                p.pp=pp
                p.interest1=i1
                p.interest2=i2
                p.interest3=i3
                p.communities1=c1
                p.communities2=c2
                p.communities=c3
                info["ppp"]=pp
                p.save()
            print(info)
    return render(request,'Profile/profile.html',{'info':info})

def Home(request):
    return render(request,'home.html')