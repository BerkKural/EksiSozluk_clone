from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def userRegister(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        name = request.POST['name']
        surname = request.POST['surname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if  User.objects.filter(username = username).exists():
                messages.error(request, 'Bu kullanıcı adı zaten mevcut')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'Bu mail adresi zaten mevcut')
            elif len(password1)<8:
                messages.error(request, 'Şifreniz en az 8 karakter olmalıdır')
            elif username.lower() in password1:
                messages.error(request, 'Şifrenizde kullanıcı adınızı kullanamazsınız')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                Profile.objects.create(
                    user = user,
                    name = name,
                    surname = surname,
                )
                messages.success(request, 'Başarıyla kayıt oldunuz')
                return redirect('index')
        else:
            messages.error(request, 'Şifreniz Uyuşmuyor')
    return render(request, 'user/register.html')

def userLogin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş Başarılı')
            return redirect('index')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre yanlış')
            return redirect('login')
    return render(request, 'user/login.html')

def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış Yapıldı')
    return redirect('index')