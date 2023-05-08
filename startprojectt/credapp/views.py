from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def Register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name= request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        Password = request.POST['Password']
        if password== Password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already Taken")
                return redirect('Register')
            else:

                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
                return redirect('login')



        else:
            messages.info(request,"Password is not matching")
            return redirect('Register')
        return redirect('/')

    return render(request,"Register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')