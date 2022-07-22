from django.shortcuts import render

from .models import Artcel

def Articel_list(request):
    articels=Artcel.objects.all() # qery or orm
    return render (request,'blog_app/Articel_list.html',context={'articels':articels})

