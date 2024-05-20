from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def home_index(request):
    return render(request,'home/homepage.html')

def login(request):
    if request.method=='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
    # messages.success(request, "Login Success Test")
    return render(request,'accounts/login.html')

def register(request):
    if request.method=='POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confpassword = request.POST.get("confpassword")
        print(first_name,last_name,email,password,confpassword)
        if password!=confpassword:
            messages.warning(request, "Password and Confirm Password doesn't match!")
    return render(request,'accounts/register.html')