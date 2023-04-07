from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def login_view(request):
    if not request.user.is_anonymous:
        messages.info(request, "Siz login qilib bo'lgansiz")
        return redirect('word:list')
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_path = request.GET.get('next')
            messages.success(request, "Muvaffaqiyatli login qildingiz")
            if next_path:
                return redirect(next_path)
            return redirect('word:index')
        return render(request, 'login.html')
    cxt = {
        'form': form
    }
    return render(request, 'login.html', cxt)


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('auth:login')
    if request.method == 'POST':
        logout(request)
        return redirect('auth:login')

    return render(request, 'logout.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('word:index')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Muvofaqiyatli ro'yhatdan o'tdingiz!")
        return redirect('auth:login')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)
