from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .forms import LoginUserForm, RegisterUserForm , EditUserProfileForm

# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home_app:home_page')
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home_app:home_page')
    else:
        form = LoginUserForm()
    return render(request, 'accounts_app\login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home_app:home_page')

# def user_register(request):
#     context={'errors':[]}
#     if request.user.is_authenticated:
#         return redirect('home_app:home_page')
#     elif request.method=='POST':
#         username=request.POST.get('username')
#         email=request.POST.get('email')
#         password1=request.POST.get('password1')
#         password2=request.POST.get('password2')
#         if password1 != password2 :
#             context['errors'].append('passwords does not match')
#             return render(request,'accounts_app/register.html',context)
#         # if User.objects.get(username=username):
#         #     context['errors'].append('this user has already exist')
#         #     return render(request,'accounts_app/register.html',context)
#         user=User.objects.create(username=username,password=password1,email=email)
#         # send mail
#         from_email = settings.EMAIL_HOST_USER
#         subject='welcome to our site'
#         message = f'hi {username} welcome to stand blog community '
#         recipient_list = [email]
#         send_mail(subject,message,from_email,recipient_list,fail_silently = False)
#         login(request,user)
#         return redirect('home_app:home_page')


#     return render(request,'accounts_app/register.html',{})


def user_register(request):
    if request.user.is_authenticated:
        return redirect('home_app:home_page')
    elif request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password_1')
            user = User.objects.create(
                username=username, email=email, password=password)
            print(user)
            login(request, user)
            return redirect('home_app:home_page')
    elif request.method == 'GET':
        form = RegisterUserForm()
    return render(request, 'accounts_app/register.html', {'form':form})



def edit_profile(request):
    user=request.user
    if request.method == 'POST':
        form=EditUserProfileForm(instance=user , data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_app:home_page')
    else:
        form=EditUserProfileForm(instance=user)
    return render (request,'accounts_app/edit_profile.html',{'form':form} )
