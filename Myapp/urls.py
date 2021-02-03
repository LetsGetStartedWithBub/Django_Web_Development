from django.urls import path, include
from .views import home,chat, bot_search, send_mail, mail, HomePageView
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('home/',home,name='home2'),
    path('',HomePageView.as_view(),name='home'),
    path('chat/',chat, name='chat'),
    path('bot_search/',bot_search, name='bot'),
    path('mail/',mail,name='mail'),
    path('send_mail/',send_mail,name='send_mail'),
    path('login/',auth_view.LoginView.as_view(template_name = 'Myapp/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name = 'Myapp/logout.html'),name='logout')
]
