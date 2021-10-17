from django.conf.urls import url

from chat.api import views

urlpatterns = [
    url(r'^messages/single/(?P<pk>\d+)/$', views.MessageDetailView.as_view(), name='message-detail'),
    url(r'^(?P<chat_slug>.+)/messages/list/(?P<paginate>\d+)/$', views.MessageListView.as_view(), name='message-list'),
    url(r'^(?P<chat_slug>.+)/messages/create/$', views.MessageCreateView.as_view(), name='message-create'),
    url(r'^list/$', views.ChatListView.as_view(), name="chat-list"),
    url(r'^(?P<slug>.+)/$', views.ChatDetailView.as_view(), name="chat-detail"),
]
