from rest_framework import generics

from chat.api.serializers import MessageSerializer
from chat.models import Chat, Message


class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        paginate_num = 10
        slug = self.kwargs["chat_slug"]
        paginate = (int(self.kwargs["paginate"]) + 1) * paginate_num
        return Message.objects.filter(chat__slug=slug).order_by('-created')[paginate-10:paginate]


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        slug = self.kwargs.get('chat_slug')
        chat = Chat.objects.get(slug=slug)

        user = self.request.user

        if user.is_authenticated:
            serializer.save(author=user, chat=chat)
        else:
            serializer.save(ip=self.request.META["REMOTE_ADDR"], chat=chat)


class MessageDetailView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
