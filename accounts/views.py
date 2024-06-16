from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from accounts.models import Profile
from products.models import PhoneList

def home_index(request):
    phones = PhoneList.objects.all()
    # images = phones.phone_images.all()
    # for x in images:
    #     print(x.image)
    return render(request,'home/homepage.html',{'phones':phones})

def login_user(request):
    redirect_to = request.GET.get('next', '')
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=email)
        if not user_obj.exists():
            messages.warning(request, "Account not found!")
            return HttpResponseRedirect(request.path_info)
            
        try:
            if not user_obj[0].profile.is_verified:
                messages.warning(request, "Your accounr is not verified")
                return HttpResponseRedirect(request.path_info)
        except Exception as e:
            print(e)
            messages.warning(request, "Invalid credentials")
            return HttpResponseRedirect(request.path_info)
            
        user_obj= authenticate(username=email,password=password)
        if user_obj:
            login(request,user_obj)
            print(redirect_to)
            return HttpResponseRedirect(redirect_to)


        messages.warning(request, "Invalid credentials")
        return HttpResponseRedirect(request.path_info)
    return render(request,'accounts/login.html')

def register(request):
    if request.method=='POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confpassword = request.POST.get("confpassword")
        print(first_name,last_name,email,password,confpassword)
        user_obj = User.objects.filter(username=email)
        if password!=confpassword:
            messages.warning(request, "Password and Confirm Password doesn't match!")
            return HttpResponseRedirect(request.path_info)
        elif user_obj.exists():
            messages.warning(request, "User already exists..Please login!")
            return HttpResponseRedirect(request.path_info)
        else:
            user_obj = User(first_name=first_name,last_name=last_name,email=email,username=email,)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Email has been send on mail.")
            return HttpResponseRedirect(request.path_info)
    return render(request,'accounts/register.html')


def activate_email(request,email_token):
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        print(e)
        return HttpResponse("Invalid Token!")

def login_page(request):

    return render(request,'accounts/login.html')

def logout_user(request):
    redirect_to = request.GET.get('next', '')
    logout(request)
    return HttpResponseRedirect(redirect_to)