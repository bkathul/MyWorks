from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return render(request,'welcome.html')
        else:
            return render(request,'login.html')

    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
            else:
                myuser = User.objects.create_user(username=username,password=password)
                myuser.save()
                return render(request,'login.html')
        else:
            messages.info(request,'Password not matching')

            return render(request,'register.html')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def welcome(request):
    return render(request,'welcome.html')


def success(request):
    return render(request,'success.html')


def detail_form(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        district = request.POST.get('district')
        branch = request.POST.get('branch')
        account_type = request.POST.get('account_type')
        material = request.POST.get('material')
        user_data = User.objects.all()
        return render(request,'success.html')
    return render(request,'details.html')
