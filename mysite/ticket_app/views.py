
from django.shortcuts import render

from . models import Ticket

def add_ticket(request):
    title=request.GET.get('title')
    email=request.GET.get('email')
    description=request.GET.get('description')
    if title and email and description:
        Ticket.objects.create(title=title,email=email,description=description)

    return render (request,'ticket_app/add_ticket.html')    
