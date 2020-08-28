from django.shortcuts import render,redirect
from regportal.models import moviereg
import json
from moviereg.models import signuptheatre
def portalform(request):
        regmail=request.session['temail']
        user=signuptheatre.objects.all().filter(email=regmail)
        for u in user:
                if u.email==regmail:
                        tname=u.tname
        if request.method=='POST':
                theatrename = tname
                moviename =request.POST.get("moviename")
                actor=request.POST.get("actor")
                actress = request.POST.get("actress")
                genre=request.POST.get("genre")
                poster=request.POST.get("poster")
                rowss=request.POST.get("rowss")
                colss=request.POST.get("colss")
                date=request.POST.get("date")
                time=request.POST.get("time")
                trailer=request.POST.get("trailer")
                tpic=request.POST.get("tpic") 
                subject=request.POST.get("subject") 
                list1=[] 
                if request.POST.get("9")=="on":
                        list1.append("9AM")
                if request.POST.get("1040")=="on":
                        list1.append("10:40 AM")
                if request.POST.get("1130")=="on":
                        list1.append("11:30 AM")
                if request.POST.get("140")=="on":
                        list1.append("1:40 PM")
                if request.POST.get("230")=="on":
                        list1.append("2:30 PM")
                if request.POST.get("340")=="on":
                        list1.append("3:40 PM")
                if request.POST.get("430")=="on":
                        list1.append("4:30 PM")
                if request.POST.get("630")=="on":
                        list1.append("6:30 PM")
                if request.POST.get("1030")=="on":
                        list1.append("10:30 M")
                #list2=str(list1)
                s=moviereg.objects.create(theatrename=theatrename,moviename=moviename,actor=actor,actress=actress,genre=genre,poster=poster,stime=json.dumps(list1),rowss=rowss,colss=colss,date=date,time=time,trailer=trailer,tpic=tpic,subject=subject)
                s.save()
                return redirect('/Moviehomepage/')
        context={
                'tname':tname
        }
        return render(request,'regportal/index.html',context)   