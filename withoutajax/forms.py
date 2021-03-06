from django import forms
from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()

class registerUserForm(UserCreationForm):
    email = forms.EmailField(required=True,help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]