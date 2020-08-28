from django.shortcuts import render,redirect
from register.models import signup 
# Create your views here.
def index(request):
    return render(request,'register/index.html')

def register(request):
        if request.method=='POST':
                username=request.POST.get("username")
                email=request.POST.get("email")
                birthdate=request.POST.get("birthday")
                gender=request.POST.get("Gender")
                pwd=request.POST.get("password")
                repwd=request.POST.get("reenterpassword")
                city=request.POST.get("city")
                phno=request.POST.get("phno")
                s=signup.objects.create(username=username,email=email,birthdate=birthdate,gender=gender,pwd=pwd,repwd=repwd,city=city,phno=phno)
                s.save()
                return render(request,'login/index.html')
        return render(request,'register/index.html')            
        