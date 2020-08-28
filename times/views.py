from django.shortcuts import render
from regportal.models import moviereg
import json
# Create your views here.
def index(request):
    moviename=request.session['movie']
    timing=moviereg.objects.all().filter(moviename=moviename)
    jsonDec = json.decoder.JSONDecoder()
    tlist={}
    for t in timing:
        tlist[t.theatrename]=jsonDec.decode(t.stime)
    studentname=request.session['semail']
    print(tlist)
    context={
        'Studentname' : studentname,
        'tname':tlist
    }
    return render(request,'times/index.html',context)