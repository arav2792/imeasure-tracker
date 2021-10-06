from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import logout


def loginview(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, 'accounts/home.html')
        else:
            return render(request, 'accounts/login.html', {'error':'Please check the creds'})
    else:
        return render(request, 'accounts/login.html')

def logoutview(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'accounts/logout.html')

@login_required
def homeview(request):
    if request.method == 'POST':
        return render(request, 'accounts/home.html')
    else:
        return render(request, 'accounts/home.html')


def forgotview(request):
    return render(request, 'accounts/password_reset_form.html')

@login_required
def usercreatedview(request):
    return render(request, 'accounts/usercreated.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:password_changed')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

@login_required
def password_changed(request):
    return render(request, 'accounts/password_changed.html')
