"""ARecSys URL Configuration
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from apps.user_authentication import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
