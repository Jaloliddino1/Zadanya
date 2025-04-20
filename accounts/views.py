from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth import login, logout



def registeratsiya(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            login(request, user)
            return redirect('phone_list')
        return render(request, 'accounts/register.html', {'form': form})

    else:
        form = UserForm()
        return render(request, 'accounts/register.html', {'form': form})



def login_user(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            login(request, user)
            return redirect('business:phone_list')
        return render(request, 'accounts/login.html', {'form': form})



def logout_user(request):
    logout(request)
    return redirect('accounts:login_user')
