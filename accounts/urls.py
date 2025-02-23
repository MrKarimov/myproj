
from django.urls import path
from .views import LoginView, RegisterView
urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('reg/',RegisterView.as_view(),name='reg'),
]