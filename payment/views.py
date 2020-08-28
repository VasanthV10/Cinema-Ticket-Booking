from django.shortcuts import render,redirect
from seats.models import seat
from regportal.models import moviereg

# Create your views here.
def payment(request):
        mv=request.session['movie']
        moviedetails=moviereg.objects.all().filter(moviename=mv)
        if request.method=='POST':
            studentname=request.session['semail']
            seats=request.POST.get("seats")
            s=seat.objects.create(seats=seats)
            s.save()
            print(studentname)
            print(seats)
            context={
                    'Studentname' : studentname,
                    'seats':seats
            }
            return redirect('/cinema/')
        return render(request,'payment/index.html')