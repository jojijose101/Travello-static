from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"User is not existed")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method  == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username):
                messages.info(request,'Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request, 'Email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,email=email,password=password)
                user.save()
                print("register sucssesfull")
                return redirect('login')
        else:
            messages.info(request, 'password doesn\'t match')
            return redirect('register')
            print("password not matching")

    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')