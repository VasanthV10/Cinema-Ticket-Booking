from django.shortcuts import render,redirect
from moviereg.models import signuptheatre
# Create your views here.
def regform(request):
        if request.method=='POST':
                email=request.POST.get("email")
                tname=request.POST.get("tname")
                pwd1=request.POST.get("psw1")
                pwd2=request.POST.get("psw2")
                if pwd1==pwd2:
                    s=signuptheatre.objects.create(email=email,tname=tname,pwd=pwd1)
                    s.save()
                    return redirect('/login/')
        return render(request,'moviereg/index.html')            
        