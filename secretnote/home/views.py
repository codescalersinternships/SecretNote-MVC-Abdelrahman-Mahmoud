from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django_ratelimit.decorators import ratelimit

# @ratelimit(key='ip', rate='100/h')
class SignUpInterfaceView(CreateView):
    template_name = 'home/signup.html'
    form_class = UserCreationForm
    success_url = '/'
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super().get(request,*args, **kwargs)
    
# @ratelimit(key='ip', rate='100/h')   
class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
        
# @ratelimit(key='ip', rate='100/h') 
class HomeView(TemplateView):
    template_name = 'home/welcome.html'


