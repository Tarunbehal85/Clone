from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('ask/', views.ask_question, name='ask'),
    path('question/<int:pk>/', views.view_question, name='view_question'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
]