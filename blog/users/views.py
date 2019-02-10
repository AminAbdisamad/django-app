# render and redirect are in django.shortcuts module
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
# For flash messages


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # save user
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account successfully created for {username}')
            # redirecting user to login page
            return redirect('user-login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    return render(request, 'users/login.html')
# different flash messages

# message.debug
# message.info
# message.success
# message.warning
# message.error
# When calling from the templates we use {message.tags} to find which tag to publish
