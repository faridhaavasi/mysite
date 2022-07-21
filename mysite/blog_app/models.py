
from django.db import models

# Create your models here.
class Artcel(models.Model):
    STATUS_CHIOCES=(
        ('p','publish'),
        ('d','dradt'),
    )
    title=models.CharField(max_length=20)
    description=models.TextField(max_length=50)
    image=models.ImageField(null=True,upload_to='blog_app')
    activate=models.BooleanField(default=True)
    status=models.CharField(default='d',choices=STATUS_CHIOCES)
    views=models.IntegerField(default=0)


    def __str__(self):
        return self.title

