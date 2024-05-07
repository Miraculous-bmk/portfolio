from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == "POST":
        get_email = request.POST.get("email")
        get_password = request.POST.get("pass1")
        get_confirm_password = request.POST.get("pass2")
        if get_password != get_confirm_password:
            messages.info(request, 'password does not match')
            return redirect('/auth/signup/')
        try:
            if User.objects.get(username=get_email):
                messages.warning(request, "Email is Taken")
                return redirect('/auth/signup/')
        except Exception as identifier:
            pass
        my_user = User.objects.create_user(get_email, get_email, get_password)
        my_user.save()
        messages.success(request, "User created successfully, please login")
        return redirect('/auth/login')
    return render(request, "signup.html")
def handleLogin(request):
    if request.method == "POST":
        get_email = request.POST.get("email")
        get_password = request.POST.get("pass1")
        my_user= authenticate(username=get_email, password=get_password)
        if my_user is not None:
            login(request, my_user)
            messages.success(request, "login successful")
            return redirect('/')
        else:
            messages.error(request, "invalid Credentials")
    return render(request, "login.html")
def handleLogout(request):
    logout(request)
    messages.success(request, "logout successful")
    return render(request, "login.html")