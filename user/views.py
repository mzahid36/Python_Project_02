from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def signup(request):
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,'index.html')
        else:
            return HttpResponse("Invalid credentials")
            return render(request,'login.html')

    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username Taken")
                # messages.info(request,"Username taken")
            elif User.objects.filter(email=email).exists():
                return HttpResponse("Email Already Exists")
                # messages.info(request,"Email Already Exists.")
            else:   
                user = User.objects.create_user(username=username,password=password1,email=email, first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,"User Created")
                return render(request,'login.html')
        else:
            return HttpResponse('Password not matching.!')
    else:
        return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')