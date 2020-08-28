from django.shortcuts import render,redirect
from contact.models import contactform
from moviereg.models import signuptheatre
# Create your views here.
def homepageview(request):
    regmail=request.session['temail']
    user=signuptheatre.objects.all().filter(email=regmail)
    #tname = user.objects.only('tname').get(email=regmail).tname
    for u in signuptheatre.objects.all():
        if u.email==regmail:
            tname=u.tname
    contact=contactform.objects.all().filter(tname=tname)
    context={
        'contact':contact,
        'user':user[0]
    }
    return render(request,'movhome/index.html',context)
