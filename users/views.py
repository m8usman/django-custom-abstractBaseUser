from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from .models import User, Profile
from .forms import CustomUserCreationForm, ProfileForm, LoginForm
from .utils import searchProfiles, paginateProfiles


class LoginUser(TemplateView):
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm()
        return context

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get()
        except:
            messages.error(request, 'email does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')

        else:
            return redirect(request.GET['next'] if 'next' in request.GET else 'login')
            messages.error(request, 'email OR password is incorrect')


class LogoutUser(View):
    def get(self, request):
        logout(request)
        messages.info(request, 'User was logged out!')
        return redirect('login')


class RegisterUser(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = '/account'


class Profiles(ListView):
    template_name = 'users/profiles.html'
    model = Profile
    context_object_name = 'profiles'


class UserProfile(DetailView):
    template_name = 'users/user-profile.html'
    model = Profile


@method_decorator(login_required, name='dispatch')
class UserAccount(TemplateView):
    def get(self, request):
        profile = request.user.profile
        context = {'profile': profile}
        return render(request, 'users/account.html', context)



@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)

