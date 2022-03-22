from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)



