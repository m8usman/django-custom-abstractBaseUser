from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'type': 'email', 'name': 'email', 'class': 'form-control', 'id': 'exampleInputEmail1',
                 'placeholder': 'Enter email'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'username', 'short_intro', 'profile_image', 'social_github']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'type': 'email', 'name': 'email', 'class': 'form-control'})
