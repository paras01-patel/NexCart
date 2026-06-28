from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.cache import never_cache
from .models import Helprequest,Report
@never_cache
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
@never_cache
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
                return redirect('populer')
            
            else:
                messages.error(req,"wrong password")
                return redirect('login')
        except:
            messages.error(req,"user not found")
            return redirect("login")
        
    return render(req, "login.html")

@never_cache
def logout(req):
    req.session.flush()
    return redirect('login')


@never_cache
def adminpanel(req):
    return render(req,'adminpanel.html')



@never_cache
def populer(req):
    return render(req,'populer.html')


def jewellery(req):
    return render(req,'jewellery.html')


def mobile(req):
    return render(req,'mobile.html')

def buynow(req):
    username = req.session.get("username")

    if username:
        return redirect("payment")
    else:
        messages.error(req, "Please login first.")
        return redirect("login")


def payment(req):
    return render(req, "payment.html")


def setting(req):
    return render(req,'setting.html')




def help(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        issue_type = request.POST.get('issue_type')
        order_id = request.POST.get('order_id')
        message = request.POST.get('message')

        data=Helprequest.objects.create(
            name=name,
            email=email,
            issue_type=issue_type,
            order_id=order_id,
            message=message,
            status="pending"
        )

        return redirect('help')

    return render(request, 'setting.html', {'help': True})


def report(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        issue_type = request.POST.get('issue_type')
        order_id = request.POST.get('order_id')
        message = request.POST.get('message')

        data=Helprequest.objects.create(
            name=name,
            email=email,
            issue_type=issue_type,
            order_id=order_id,
            message=message,
            status="pending"
        )

        return redirect('reprot')

    return render(request, 'setting.html', {'help': True})

def report_is(request):
    reports = Report.objects.all()
    return render(request, 'adminpanel.html', {'report_is': True,'reports': reports})



def help_is(req):
    helps=Helprequest.objects.all()
    return render(req,'adminpanel.html',{'help_is':True,'helps':helps})