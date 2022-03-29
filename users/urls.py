from django.urls import path
from django.contrib.auth import views as auth_views
from .views import send_student_mail

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True,
		template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('send/student/<int:pk>/mail/', send_student_mail, name='send_student_mail')
]
