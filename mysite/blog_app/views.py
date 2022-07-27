

from django.shortcuts import render ,redirect

from .models import Artcel

def home(request):
    return render (request,'blog_app/home.html')


def Articel_list(request):
    articels=Artcel.objects.all() # qery or orm
    return render (request,'blog_app/Articel_list.html',context={'articels':articels})

def detail(request,id):
    articel=Artcel.objects.get(id=id)
    articel.views+=1
    articel.save()
    return render (request,'blog_app/detail.html',{'articel':articel})

def add_articel(request):
    #title=request.GET.get('title')
    #description=request.GET.get('description')
    #print(title)
    #print(description)
    # method POST
    if request.method=="POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        if title and description:
            Artcel.objects.create(title=title,description=description)
            return redirect('/articel_list')
             
 

    return render (request,'blog_app/add_article.html')
