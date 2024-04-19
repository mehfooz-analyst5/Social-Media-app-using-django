from django.shortcuts import redirect, render, HttpResponse
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserEditForm, ProfileEditForm
from posts.models import Post

# Create your views here.



def index(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    posts = Post.objects.filter(author=current_user)
    return render(request, 'users/index.html', {'posts': posts, 'profile': profile})
     

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                # Process the data in form.cleaned_data
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')
                else:
                    return redirect('login')
                
        else:
            form = LoginForm()

        return render(request, 'users/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('index')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')






@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

    return render(request, 'users/edit.html', {'user_form': user_form, 'profile_form': profile_form})