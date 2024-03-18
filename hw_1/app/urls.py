from django.urls import path
from .views import context_handler
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', context_handler),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]