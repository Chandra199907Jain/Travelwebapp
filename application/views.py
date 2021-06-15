from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import Register

# Create your views here.
def index(request):
    return render(request,"application/index.html")
def register(request):
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]

        values ={
            'name':name,'email':email,'password':password
        }
        registers=Register(name="name",email="email",password="password")
        error_message = None
        if len(registers.name) <2:
            error_message = "Please enter a suitable name"
        if len(password)<8:
            error_message="Password should be more than 8 characters"

        if not error_message:
            if Register.objects.filter(name=name).exists():
                error_message = 'Username taken'
                return redirect("/register")
            elif Register.objects.filter(email=email).exists():
                error_message="Email taken"
                return redirect("/register")
            else:
                registers.password = make_password(registers.password)
                registers.save()
                print("No errors")
                return redirect("/index")
        else:
            data = {
                'error':error_message,'values':values
                 }
            print("Errors")
            return render(request,"application/register.html",data)

        return redirect("/index")

        
    else:
      print("GET Request")
      return render(request,"application/register.html")
def login(request):
    return render(request,"application/login.html")
