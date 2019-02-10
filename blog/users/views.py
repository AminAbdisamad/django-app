# render and redirect are in django.shortcuts module
from django.shortcuts import render, redirect
# For flash messages
from django.contrib import messages
# login required decorators
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # save user
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Congrats {username}! Your Account hass been successfully created.')
            # redirecting user to login page
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    return render(request, 'users/login.html')

# After we set login_required it'll automatically redirect to account/login
#  so we'll change the URL in the setting eg (LOGIN_URL = 'login')
@login_required
def profile(request):
    return render(request, 'users/profile.html')
# different flash messages
# message.debug
# message.info
# message.success
# message.warning
# message.error
# When calling from the templates we use {message.tags} to find which tag to publish
