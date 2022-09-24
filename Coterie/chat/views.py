from django.shortcuts import render
from login.models import Profile

from django.forms.models import model_to_dict

# Create your views here.            
def chatPage(request,*args,**kwargs):
    context={}
    lst=[]
    userActive=False
    id=kwargs['id']
    p1=[]
    p2=[]
    p=Profile.objects.filter(token=id).first()
    if p:
        p=model_to_dict(p)
        if p['activeChat1'] or p['activeChat2'] or p['comChat1'] or p['comChat2']:
            userActive=True
            p1=Profile.objects.filter(token=p['activeChat1']).first()
            if p1:
                p1=model_to_dict(p1)
                lst.append(p1)
            p2=Profile.objects.filter(token=p['activeChat2']).first()
            if p2:
                p2=model_to_dict(p2)
                lst.append(p2)
            c1=Profile.objects.filter(token=p['comChat1']).first()
            if c1:
                c1=model_to_dict(c1)
                lst.append(c1)
            c2=Profile.objects.filter(token=p['comChat2']).first()
            if c2:
                c2=model_to_dict(c2)
                lst.append(c2)

    searchQuery=request.POST.get("searchQuery")
    if searchQuery:
        p=Profile.objects.filter(username=searchQuery).first()
        p2=Profile.objects.filter(token=id).first()
        if p:
            if p.activeChat1 != id:
                temp=p.activeChat1
                p.activeChat1=id
                p.activeChat2=temp
            if p2.activeChat1 != p.token:
                temp=p2.activeChat1
                p2.activeChat1=p.token
                p2.activeChat2=temp
            p2.save()
            p2=model_to_dict(p2)
            p.save()
            p=model_to_dict(p)  
            lst.append(p)
    return render(request,'Chat/chat.html',{'userActive':userActive,'lst':lst,'u1':p1,'sname':p2})