from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    studentname=request.session['semail']
    context = {
        'Studentname' : studentname,
    }
    return render(request,'aboutus/aboutus.html',context)