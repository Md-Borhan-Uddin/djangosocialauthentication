from django.urls import path
from loginapp import views


urlpatterns = [
   path('', views.HomeTemplateView.as_view()),
   # path('login', views.LoginView.as_view()),
]
