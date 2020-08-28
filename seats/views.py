from django.shortcuts import render,redirect
from seats.models import seat
from regportal.models import moviereg

# Create your views here.
def index(request):
    return render(request,'seats/index.html')
def Book(request):
        mv=request.session['movie']
        moviedetails=moviereg.objects.all().filter(moviename=mv)
        if request.method=='POST':
            seats=request.POST.get("seats")
            s=seat.objects.create(seats=seats)
            s.save()
            return redirect('/cinema/')
        return render(request,'seats/index.html')