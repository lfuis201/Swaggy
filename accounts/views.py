from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import NewUSerForm

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required
from .forms import UserEditForm

from .forms import CustomAuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form = NewUSerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:home')
    else:
        form = NewUSerForm()
    return render(request, 'accounts/signup.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('main:home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def logout_view(request):
    if request.method == 'POST':
            logout(request)
            return redirect('/')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('main:home')  # Reemplaza 'main:profile' con la URL de la página de perfil
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})

        
class CustomPasswordResetView(PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset_email.html'
