from django.shortcuts import render, redirect
from django.http import HttpResponse, QueryDict
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# Remember that you are not signed in as admin or else elcome page will open

def home(request):
    messages.info(request,"Hello nik!!")
    return render(request, 'home.html')

def signin(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=uname):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('/signin')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('/signin')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('/signin')
        
        newUser = User.objects.create_user(uname,email,pass1)
        newUser.first_name = fname
        newUser.last_name = lname
        newUser.save()
        login(request,newUser)
        # messages.success(request, "Your account has been successfully created!!")
        return redirect('welcome')
    return render(request, 'signin.html')

def logIn(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        user = authenticate(username=uname, password=passwd)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request,"Invalid Credentials!!")
    return render(request,'login.html') # incase a person directly changes the url

def welcome(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        messages.error(request,"Please SignIn!!")
    return render(request, 'welcome.html',{'uname':request.user.username})
    # these is called a dictionary(context) which is used to pass parameters to use them in front-end templates

def logOut(request):
    if not request.user.is_anonymous:
        logout(request)
    return redirect('/')


def notfound(request,nik):
    return HttpResponse("Error 404: Page Not Found")

    