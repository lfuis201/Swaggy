from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import PasswordChangeForm


class CustomSignupForm(UserCreationForm):

    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
    'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
    'placeholder': 'Username',
}))

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
        'placeholder': 'Email address',
    }))
    phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
        'placeholder': 'Phone number',
    }))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
        'placeholder': 'First name',
    }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
        'placeholder': 'Last name',
    }))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
        'placeholder': 'Password',
    }))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
        'placeholder': 'Confirm password',
    }))

    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomSignupForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class UserEditForm(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
        'placeholder': 'Username',
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
        'placeholder': 'Email address',
    }))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
        'placeholder': 'First name',
    }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
        'placeholder': 'Last name',
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
        'placeholder': 'Email address',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
        'placeholder': 'Password',
    }))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-checkbox text-blue-600',
    }))

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
        'placeholder': 'Current password',
    }))
    new_password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
        'placeholder': 'New password',
    }))
    new_password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
        'placeholder': 'Confirm new password',
    }))
