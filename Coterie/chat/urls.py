from django.urls import path,include
from chat import views

urlpatterns=[
    path("<int:id>",views.chatPage,name='chat-page'),
]