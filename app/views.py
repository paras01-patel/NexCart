from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def home(req):
    return render(req, 'home.html')

def signup(req):
    if req.method == "POST":

        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(req, "Password does not match")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(req, "Email already exists")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(req, "Username already exists")
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        messages.success(req, "Signup Successfully")
        return redirect('login')

    return render(req, 'signup.html')
def login(req):
    if req.method == "POST":

        username = req.POST.get('username')
        password = req.POST.get('password')

        try:
            user = User.objects.get(username=username)

            if user.check_password(password):
                req.session['username'] = user.username
                messages.success(req, "Successfully Login")
                return redirect('home')

            else:
                messages.error(req, "Wrong Password")
                return redirect('login')

        except User.DoesNotExist:
            messages.error(req, "User Found")
            return redirect('login')

    return render(req, 'login.html')