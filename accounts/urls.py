from django.urls import path, include
from . import views
from .views import CustomPasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView,PasswordResetDoneView

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),


    path('edit-profile/', views.edit_profile, name='edit_profile'),


]
