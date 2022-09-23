from django.shortcuts import render

# Create your views here.
def chatPage(request,*args,**kwargs):
    context={}
    return render(request,'Chat/chat.html',context=context)
