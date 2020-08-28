from django.shortcuts import render, redirect
from django.http import HttpResponse
from contact.models import contactform 
# Create your views here.
def index(request):
    return render(request,'contact/contact.html')
def contactus(request):
    studentname=request.session['semail']
    context = {
        'Studentname' : studentname,
    }
    if request.method=='POST':
            tname=request.POST.get("tname")
            fname=request.POST.get("fname")
            lname=request.POST.get("lname")
            content=request.POST.get("content")
            s=contactform.objects.create(tname=tname,fname=fname,lname=lname,content=content)
            s.save()
            return redirect('/cinema/',context)
    return render(request,'contact/contact.html',context)   