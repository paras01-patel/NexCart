from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


# SIGNUP

def home(req):
    return render(req,'home.html')


def signup(req):
    if req.method == "POST":
        username = req.POST.get('username')
        email = req.POST.get('email')
        password1 = req.POST.get('password1')
        password2 = req.POST.get('password2')

        # PASSWORD CHECK

        if password1 != password2:

            messages.error(req, "Password does not match")
            return redirect('signup')

        # USERNAME CHECK

        if User.objects.filter(username=username).exists():

            messages.error(req, "Username already exists")
            return redirect('signup')

        # EMAIL CHECK

        if User.objects.filter(email=email).exists():

            messages.error(req, "Email already exists")
            return redirect('signup')

        # CREATE USER

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        user.save()

        messages.success(req, "Signup Successfully")

        return redirect('login')

    return render(req, 'signup.html')


# LOGIN PAGE

def login(req):
    if req.method=="POST":
        username=req.POST.get('username')
        password=req.POST.get('password')
        
        if username == "admin" and password == "1234":
            req.session['username'] = username
            messages.success(req, "Login Successful")
            return redirect('adminpanel')
        
        try:
            user= User.objects.get(username=username)
            if user.check_password(password):
                req.session['username']=user.username
                messages.success(req,"successfully login ")
                return redirect('home')
            
            else:
                messages.error(req,"wrong password")
                return redirect('login')
        except:
            messages.error(req,"user not found")
            return redirect("login")
        
    return render(req, "login.html")

def logout(req):
    req.session.flush()
    return redirect('login')

def adminpanel(req):
    return render(req,'adminpanel.html')