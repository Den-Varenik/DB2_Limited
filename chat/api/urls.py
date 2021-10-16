from django.conf.urls import url

from chat.api.views import MessageListView, MessageCreateView, MessageDetailView

urlpatterns = [
    url(r'^(?P<chat_slug>.+)/messages/list/(?P<paginate>\d+)/$', MessageListView.as_view(), name='message-list'),
    url(r'^(?P<chat_slug>.+)/messages/create/$', MessageCreateView.as_view(), name='message-create'),
    url(r'^(?P<chat_slug>.+)/messages/single/(?P<pk>\d+)/$', MessageDetailView.as_view(), name='message-detail'),
]
