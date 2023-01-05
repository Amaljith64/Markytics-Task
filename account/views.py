from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def home(request):
    print('hii')
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "":
            messages.error(request, "Fill all fields")
            return redirect(login)

        if password == "":
            messages.error(request, "Fill all fields")
            return redirect(login)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have succesfully logged in')
            return redirect(home)
        else:
            messages.error(request, "Invalid Credentials")
            return redirect(login)
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        password1 = request.POST["password1"]
        if password1 != "":
            password2 = request.POST["password2"]
            if password1 == password2:
                username = request.POST["username"]
                if username == "":
                    messages.error(request, "username is empty")
                    return redirect(signup)
                elif User.objects.filter(username=username):
                    messages.error(request, "username exits")
                    return redirect(signup)
                User.objects.create_user(username=username, password=password1)
                messages.success(
                    request, "Registration successful. Please login")
                return redirect(login)
            else:
                messages.error(request, "Password Not match")
                return redirect(signup)
        else:
            messages.error(request, "please fill all fields")
            return redirect(signup)

    return render(request, 'signup.html')
