from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    return render(request,'home.html')


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password =request.POST.get('password')
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'Invaid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,
                first_name=first_name,last_name=last_name)
                user.save()
                print('user added')
                return redirect('login')
        else:
            messages.info(request,'password not maching..')
            return redirect ('signup')
            
        return redirect('/')


    else:   
        return render(request,'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
