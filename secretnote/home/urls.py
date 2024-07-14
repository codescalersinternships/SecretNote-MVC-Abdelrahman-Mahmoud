from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('login/', views.LoginInterfaceView.as_view(), name="login"),
    path('logout/', views.LogoutInterfaceView.as_view(), name="logout"),
    path('signup/', views.SignUpInterfaceView.as_view(), name="signup"),
    
    path('postlogout/', views.LogoutView.as_view(next_page='home'), name='postlogout'),
]