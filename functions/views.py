from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from functions.models import Courses, Teachers


def index(request):


    courses = Courses.objects.all()
    teachers = Teachers.objects.all()

    return render(request, 'home.html', {"course": courses, "teacher": teachers})


def register(request):
    if request.method == 'POST':
        first_name = request.POST['fName']
        Last_name = request.POST['lName']
        username = request.POST['uName']
        password1 = request.POST['pwd1']
        password2 = request.POST['pwd2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name is already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=Last_name,
                    password=password1,
                    email=email,
                    username=username,
                )
                user.save()
                messages.info(request,'user name is created')
                return redirect('login')
        else:
            messages.info(request,'password not matching')

            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method =='POST':
        username = request.POST['uName']
        password = request.POST['pwd']

        user = auth.authenticate(username =username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid input')
            redirect('login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

