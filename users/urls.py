from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register_user_type, name='register_user_type'),
    path('register/teacher/', views.register_teacher, name='register_teacher'),
    path('register/student', views.register_student, name='register_student'),
    path('login', views.login_view, name='login'),
    path('', views.logout_view, name='logout'),
    path('profile', views.profile_view, name='profile'),
    path('registration_success/', views.registration_success, name='registration_success'),
]
