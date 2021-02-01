from django.urls import path, include
from .views import home,chat, bot_search, send_mail, mail

urlpatterns = [
    path('',home,name='home'),
    path('chat/',chat, name='chat'),
    path('bot_search/',bot_search, name='bot'),
    path('mail/',mail,name='mail'),
    path('send_mail/',send_mail,name='send_mail')
]
