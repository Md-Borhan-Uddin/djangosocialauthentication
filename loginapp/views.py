from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
# Create your views here.

class HomeTemplateView(TemplateView):
    
    template_name = 'loginapp/home.html'



class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'loginapp/login.html')
    

    def post(self, request, *args, **kwargs):
        return redirect('/')