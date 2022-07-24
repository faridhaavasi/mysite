from django.db import models

class Ticket(models.Model):
    title=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    description=models.TextField()


    def __str__(self):
        return self.title
    
