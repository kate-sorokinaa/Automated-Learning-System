from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.about, name='courses'),
    path('profile/', views.about, name='profile'),
    path('login/', views.user_login, name='login'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
]
