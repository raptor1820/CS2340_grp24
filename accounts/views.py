from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth import login as user_login, logout as user_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# need to make home app, redirect there on correct form.

def sign_up(request):
    template_data = {}
    template_data['title'] = 'Sign Up'

    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {"template_data": template_data})

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {"form": form})


def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html',{'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html',{'template_data': template_data})
        else:
            user_login(request, user)
            return redirect('home.index')


@login_required
def logout(request):
    user_logout(request)
    return redirect('home.index')


@login_required
def orders(request):
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html',
        {'template_data': template_data})