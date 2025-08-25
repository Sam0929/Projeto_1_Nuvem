from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from .views import home, profile, RegisterView, LoginAndRegisterView, ResetPasswordView, ChangePasswordView
from .forms import LoginForm

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),

    # Autenticação
    path('login/', LoginAndRegisterView.as_view(), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    # Social Auth
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),

]
