from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Context
from django.contrib.auth.models import User
from login import views
from regportal.models import moviereg
from django.contrib.auth import authenticate, login
from register.models import signup 
import json
# Create your views here.
def homepage(request):
    if 'semail' not in request.session:
       request.session['semail']=None
    if 'temail' not in request.session:
       request.session['temail']=None
    if request.session['temail']!=None:
        return redirect('/Moviehomepage/')
    studentname=request.session['semail']
    gen=signup.objects.all().filter(email=studentname)
    dict1={}
    listtemp=[]
    list1=[]
    list2=[]
    if request.session['semail']==None:
            Movi = moviereg.objects.all().order_by('date')
            Movie=reversed(Movi)
            for mv in Movie:
                    if mv.moviename in list1:
                        print(mv.moviename)
                    else:
                        list1.append(mv.moviename)
                        list2.append(mv)
    else:
        for g in gen:
            if g.genreview=='none':
                Movi = moviereg.objects.all().order_by('date')
                Movie=reversed(Movi)
                for mv in Movie:
                        if mv.moviename in list1:
                            print(mv.moviename)
                        else:
                            list1.append(mv.moviename)
                            list2.append(mv)
            else:
                jsonDec = json.decoder.JSONDecoder()
                genre = jsonDec.decode(g.genreview)
                print(genre)
                for g in genre:
                    if g in dict1:
                        dict1[g]+=1
                    else:
                        dict1[g]=1
                sortdict=sorted(dict1.items(), key = lambda kv:(kv[1], kv[0]))
                result=[]
                for t in sortdict[::-1]: 
                    for x in t: 
                        result.append(x) 
                        break
                temp1=moviereg.objects.all().filter(genre=result[0])
                listtemp.append(moviereg.objects.all().filter(genre=result[0]).order_by('date'))
                for r in result[1:]:
                    print(r)
                    listtemp.append(moviereg.objects.all().filter(genre=r).order_by('date'))
                    temp=moviereg.objects.all().filter(genre=r)
                    #print(temp)
                    temp1=temp.union(temp1)
                temp2=moviereg.objects.all()
                temp2=temp2.difference(temp1)
                print(temp2)
                listtemp.append(temp2)
                #print(temp)
                Movie=listtemp    
                for m in Movie:
                    for mv in m:
                        if mv.moviename in list1:
                            print(mv.moviename)
                        else:
                            list1.append(mv.moviename)
                            list2.append(mv)
    #return HttpResponse(studentname)
    context = {
        'Movie' : list2
    }
    if(request.session.get('email',None)):
        return render(request,'cinema/homepage.html',context)
    else:
        context['Studentname']=studentname
    if request.method=='POST':
        request.session['movie']=request.POST.get("mvname")
        return redirect('/knowmore/')
    return render(request,'cinema/homepage.html',context)