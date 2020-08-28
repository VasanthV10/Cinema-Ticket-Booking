from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Context
from django.db import models
from register.models import signup
#from contact.models import contactform 
# Create your views here.

def pro(request):
    if request.session['semail']!=None:
            #name=request.POST.get("fname")
            #email=request.POST.get("lname")
            #content=request.POST.get("content")
            #s=contactform.objects.create(fname=fname,lname=lname,content=content)
            #s.save()
            #return redirect('/cinema/')
        studentname=request.session['semail']
        data=signup.objects.all().filter(email=studentname)
        print(data)
        #for d in data:
        #    if studentname==data.email:

        context = {'Studentname' : studentname,
        'Data':data,
        }
        if request.method=='POST':
            uname=request.POST.get("name")
            bdate=request.POST.get("bday")
            mail=request.POST.get("email")
            request.session['semail']=mail
            phnno=request.POST.get("phno")
            signup.objects.all().filter(email=studentname).update(username=uname,birthdate=bdate,email=mail,phno=phnno)
            return redirect('/cinema/')
        return render(request,'userprofile/index.html',context)
    return redirect('/cinema/')