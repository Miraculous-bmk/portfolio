from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Contact,Blogs

# Create your views here.
def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def handleblog(request):
    posts=Blogs.objects.all()
    context={"posts": posts}
    return render(request, "blog.html", context)
def contact(request):
    if request.method=="POST":
        f_name=request.POST.get('name')
        f_email=request.POST.get('email')
        f_phone=request.POST.get('num')
        f_desc=request.POST.get('desc')
        query=Contact(name=f_name,email=f_email,phone_number=f_phone,description=f_desc)
        query.save()
        messages.success(request, "Thanks for contacting us. We will get back to you soon!")

        return redirect('/contact')
    return render(request, "contact.html")
    
def services(request):
    return render(request, "services.html")
