from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username = request.POST['username']
        email    = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            user = User.objects.create_user(username=username,password=password,email=email,
                                            first_name=first_name,last_name=last_name)
            user.save()
            return redirect('login')
        else:
            messages.ERROR(request,'passwords do not match')
            return redirect('register')

    return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
    return render(request,'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request,'accounts/dashboard.html')
