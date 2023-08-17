from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.decorators.cache import never_cache




# Create your views here.
@never_cache
def HomePage(request):
    if 'username' in request.session:
        return render(request, 'home.html')
    return redirect('login')




def SignupPage(request):
    if 'username' in request.session:
        return render(request, 'home.html')
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1!=pass2:
            messages.error(request, 'password is not matching')
            return redirect('signup')
            # return HttpResponse("password is not matching")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request,'signup.html')

@never_cache
def LoginPage(request):
    if 'username' in request.session:
        return redirect('home')
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)

        if user is not None:
            # login(request,user)
            request.session['username'] = username
            return render(request,'home.html')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
        # print(username,pass1)

    return render(request, 'login.html')
@never_cache
def LogoutPage(request):
    # logout(request)
    if 'username' in request.session:
        request.session.flush()
    return redirect('login')
