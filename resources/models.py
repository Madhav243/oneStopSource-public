from django.db import models
from django.utils import timezone
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.

class Topic(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=200,unique=True)
    description=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    pic=CloudinaryField('image')

    def __str__(self):
        return self.title

class SubTopic(models.Model):
    topic=models.ForeignKey('resources.Topic',on_delete=models.CASCADE)
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    link=models.URLField(blank=True)
    description=models.TextField()
    
    create_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Subscription(models.Model):
    email=models.EmailField(max_length=254)





class Request(models.Model):
    status_choices=(
        ("P","Pending"),
        ("A","Approved"),
        ("R","Rejected")
    )
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE,default=1)
    
    newResourceTitle=models.CharField(max_length=200,default='')
    description=models.TextField(max_length=1000,default='')
    create_date=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=1,choices=status_choices,default="P")

    def __str__(self):
        return "Requested Resource : " + self.newResourceTitle 



