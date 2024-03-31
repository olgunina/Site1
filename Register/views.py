from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect


from Register.forms import UserRegisterForm, UserLoginForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация успешна')
            user = form.save()
            login(request, user)
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home1')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


# def login(request):
#   return render(request, 'Human/login.html')


def user_logout(request):
    logout(request)
    return redirect('Login')
