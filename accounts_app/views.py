from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm,UserEditForm



def user_login(request):

    if request.user.is_authenticated == True:
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request,user)
            return redirect('home_app:home_page')
    else:
        form = LoginForm()
    return render(request,'accounts_app/login.html',{'form':form})






def user_register(request):
    
    if request.user.is_authenticated == True:
        return redirect('/')
    
    if request.method =='POST':
        comtext ={'errors': []}
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user=User.objects.create(username=username,email=email,password=password1)
        login(request,user)
        return redirect('/')
        
    return render(request,'accounts_app/register.html')


def user_edit(request):
    user = request.user
    form = UserEditForm(instance=user)
    if request.method == 'POST':
        form = UserEditForm(data=request.POST,instance=user)
        if form.is_valid():
            form.save()
    return render(request,'accounts_app/edit.html',context={'form':form})

def user_logout(request):
    logout(request)
    return redirect('/')
