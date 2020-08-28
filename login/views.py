from django.shortcuts import render,redirect  
from django.http import HttpResponse 
from register.models import signup
from moviereg.models import signuptheatre
from django.contrib.auth.models import User
from contact.models import contactform
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    return render(request,'login/index.html')

def loginform(request):
        if request.session['semail']==None:
                users = signup.objects.all()
                movieusers=signuptheatre.objects.all()
                for movuser in movieusers:
                        print(movuser.email,request.POST.get("email"),movuser.pwd,request.POST.get("password"))
                        if(movuser.email == request.POST.get("email") and movuser.pwd == request.POST.get("psw")):
                                request.session['temail'] = request.POST.get("email")                                 
                                return redirect('/Moviehomepage/')           
                for user in users:
                        print(user.email,request.POST.get("email"),user.pwd,request.POST.get("password"))
                        if(user.email == request.POST.get("email") and user.pwd == request.POST.get("psw")):
                                request.session['semail'] = request.POST.get("email") 
                                return redirect('/cinema/')           
                return render(request,'login/index.html')
        else:
                return redirect('/cinema/')          
def signout(request):
        if request.session['semail']==None:
                request.session['temail']=None
        else:
                request.session['semail']=None
        return redirect('/cinema/')