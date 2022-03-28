from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html'), name='login')
]