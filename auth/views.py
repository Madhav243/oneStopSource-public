
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    error=''
    if request.method == 'POST':
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        
        if user:
            auth_login(request,user)
            return HttpResponseRedirect('/')
        else:
            error='Invalid Username/Password'
    context={
        'error':error
    }
        
    return render(request,'registration/login.html',context)


def signup(request):
    error=''
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username,email,password)
        if user is None:
            error='Some error occured. Please try again !'
        else:
            user.last_name=last_name
            user.first_name=first_name
            user.save()
            
            return redirect('/auth/login')

    context={
        'error':error
    }
    return render(request,'registration/signup.html',context)


def auth_logout(request):
    logout(request)
    return redirect('/auth/login')