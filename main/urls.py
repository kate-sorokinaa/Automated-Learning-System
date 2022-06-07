from django.urls import path

import courses.views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', courses.views.courses_home, name='courses'),
    path('login/', views.user_login, name='login'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
]
