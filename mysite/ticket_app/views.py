
from django.shortcuts import render,redirect

from . models import Ticket

def add_ticket(request):
    if request.method=="POST":
        title=request.POST.get('title')
        email=request.POST.get('email')
        description=request.POST.get('description')
        if title and email and description:
            Ticket.objects.create(title=title,email=email,description=description)
            

    return render (request,'ticket_app/add_ticket.html')    
