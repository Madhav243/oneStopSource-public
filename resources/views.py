from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from resources import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.



@login_required(login_url='/auth/login')
def index(request):
    return render(request,'resources/index.html')

@login_required(login_url='/auth/login')
def viewTopics(request):
    topics = models.Topic.objects.all()
    context={
        'topics':topics
    }
    return render(request,'resources/topics.html',context)

@login_required(login_url='/auth/login')
def subtopics(request,pk):
    subtopics=models.SubTopic.objects.filter(topic=pk)
    topic=models.Topic.objects.get(id=pk)
    context={
        'topic':topic.title,
        'subtopics':subtopics
    }

    return render(request,'resources/subTopics.html',context)


@login_required(login_url='/auth/login')
def profile(request):
    requests=models.Request.objects.filter(user=request.user)

    context={
        'requests':requests
    }

    return render(request,'resources/profile.html',context)


@login_required(login_url='/auth/login')
def search(request):

    if request.method=='POST':
        topic=request.POST['searchedTopic']
        topics=models.Topic.objects.filter(title__startswith=topic)
        context={
            'topic':topic,
            'topics':topics
        }
        return render(request,'resources/search.html',context)


@login_required(login_url='/auth/login')
def subscribe(request):
    if request.method=='POST':
        email=request.POST['subscription_email']
        user=models.Subscription.objects.create(email=email)
        user.save()
        success=''
        if user:
            success='Subscribed Successfully'
        
        context={
            'success':success
        }
        return render(request,'resources/index.html',context)


@login_required(login_url='/auth/login')
def request_form(request):
    if request.method=='POST':
        newTopic=request.POST['newTopic']
        description=request.POST['description']
        requested_topic=models.Request.objects.create(newResourceTitle=newTopic,description=description,user=request.user)
        if requested_topic:
            users=User.objects.filter(is_staff=True)
            for user in users:
                subject = 'New Topic is Requested at oneStopSource '
                message = f'Hi {user.username}, new request for topic {newTopic} is added , please review the request .'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail( subject, message, email_from, recipient_list )
            requested_topic.save()
            return render(request,'resources/profile.html',{'success':'Requested Successfully'})
        else:
            return render(request,'resources/add_request_form.html',{'error':'Some error occured. Please try again !'})



    return render(request,'resources/add_request_form.html')