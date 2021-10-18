from django.test import SimpleTestCase
from django.urls import reverse, resolve

from chat.api import views


class ChatAPIUrlsTest(SimpleTestCase):

    def test_chat_list(self):
        url = reverse("chat-list")
        self.assertEquals(resolve(url).func.view_class, views.ChatListView)

    def test_chat_details(self):
        url = reverse("chat-details", args=("slug",))
        self.assertEquals(resolve(url).func.view_class, views.ChatDetailView)


class MessageAPIUrlsTest(SimpleTestCase):

    def test_message_list(self):
        url = reverse("message-list", args=("chat_slug", 0))
        self.assertEquals(resolve(url).func.view_class, views.MessageListView)

    def test_message_details(self):
        url = reverse("message-details", args=(0,))
        self.assertEquals(resolve(url).func.view_class, views.MessageDetailView)

    def test_message_create(self):
        url = reverse("message-create", args=("chat_slug",))
        self.assertEquals(resolve(url).func.view_class, views.MessageCreateView)