from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import AuthUser, RegisterForm
from .models import Profile
from django.contrib.auth.models import User


def logout_view(request):
    logout(request)
    return redirect('/')

class LoginView(View):
    def get(self, request):
        form = AuthUser()
        context = {'form': form}
        return render(request, 'app_user/login.html', context=context)

    def post(self, request):
        form = AuthUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    form.add_error('__all__', 'Учетная запись не активна.')
            else:
                form.add_error('__all__', 'Неверно введены имя пользователя или пароль.')
        context = {'form': form}
        return render(request, 'app_user/login.html', context=context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.data)
        if form.is_valid():
            user = form.save()
            slug = form.cleaned_data.get('slug')
            city = form.cleaned_data.get('city')
            school = form.cleaned_data.get('school')
            grade = form.cleaned_data.get('grade')
            Profile.objects.create(user=user, slug=slug, city=city, school=school, grade=grade)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'app_user/register.html', context=context)
    else:
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'app_user/register.html', context=context)


def profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    profile = get_object_or_404(Profile, user=user)
    print(profile)
    context = {
        'profile': profile
    }
    return render(request, 'app_user/profile.html', context=context)
