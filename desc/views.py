from django.shortcuts import render,redirect
from .models import actorpic,actresspic
from regportal.models import moviereg
# Create your views here.
def descview(request):
    if request.method=='POST':
        return redirect('/times/')
    mv=request.session['movie']
    moviedetails=moviereg.objects.all().filter(moviename=mv)
    a=moviedetails[0].actor
    as1=moviedetails[0].actress
    print(a)
    print(as1)
    alink=actorpic.objects.all().filter(aname=a)
    aslink=actresspic.objects.all().filter(asname=as1)
    context={
        'link':moviedetails[0],
        'alink':alink[0],
        'aslink':aslink[0]
    }
    return render(request,'desc/index.html',context)

