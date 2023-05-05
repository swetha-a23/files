from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.template import context,Template

def home(request):
    return render(request,"home.html")

def register(request):    
    if request.method=='POST':
        name=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1==password2:        
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.save()
            messages.success(request,'Your account has been created! You are able to login now')
            return redirect('Login')
        else:
            messages.warning(request,'Password Mismatching...!')
            return redirect('Register')        
    else:
        form=CreateUserForm()        
        return render(request,"register.html",{'form':form})
    
@login_required
def profile(request):
    return render(request,"profile.html")

def loginaft(request):
   if request.method=='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return render(request,"home.html")      
        else:
            messages.warning(request,'Username or password is incorrect')
            return redirect('Login')          
   else:
       return redirect('/')
   

def submit(request):
    Ans1=request.GET["Ans1"]
    Ans2=request.GET["Ans2"]
    Ans3=request.GET["Ans3"]
    Ans4=request.GET["Ans4"]
    return render(request,"output.html",{'Ans1':Ans1,'Ans2':Ans2,'Ans3':Ans3,'Ans4':Ans4})
