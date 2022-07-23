

from django.shortcuts import render 

from .models import Artcel

def home(request):
    return render (request,'blog_app/home.html')


def Articel_list(request):
    articels=Artcel.objects.all() # qery or orm
    return render (request,'blog_app/Articel_list.html',context={'articels':articels})

def detail(request,id):
    articel=Artcel.objects.get(id=id)
    return render (request,'blog_app/detail.html',{'articel':articel})