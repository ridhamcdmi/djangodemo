from django.shortcuts import render

# Create your views here.

def getdata(req):
    return render(req,"home.html")