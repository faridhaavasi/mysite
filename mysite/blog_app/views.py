from django.shortcuts import render

from .models import Artcel

def Articel_list(request):
    articel=Artcel.objects.all() # qery or orm
    return render (request,'blog_app/Artcel_list.html',context={'articel':articel})
     
