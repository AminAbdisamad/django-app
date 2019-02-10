from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    # by default its required  to make it optional required = false
    email = forms.EmailField()

    # This class Meta will give us nested name space for configuration
    # and keeps configurations in one place, in the configuration it will
    #  effect user model eg, form.save() it'll save on user model
    class Meta:
        # This form will interact with user model, that means whenever
        # This form is validated it will create a new user
        model = User
        fields = ['username', 'email', 'password1', 'password2']
