from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from chat.models import Chat, Message


User = get_user_model()


class MessageTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.chat = Chat.objects.create(title="Test",
                                        slug="test",
                                        description="Chat for test",
                                        public=True)
        self.message = Message.objects.create(ip="127.0.0.1",
                                              email="test@mail.ru",
                                              text="Test message",
                                              chat=self.chat)

    def test_message_list(self) -> None:
        response = self.client.get(reverse("message-list", args=(self.chat.slug, 0)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_message_details(self) -> None:
        response = self.client.get(reverse("message-details", args=(self.message.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_message_create(self) -> None:
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse("message-create", args=(self.chat.slug,)), data={"email": "test@mail.ru",
                                                                                             "text": "Create message"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.filter(chat=self.chat).count(), 2)
        self.assertEqual(Message.objects.latest('created').author, None)
        self.assertEqual(Message.objects.latest('created').ip, "127.0.0.1")

        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse("message-create", args=(self.chat.slug,)), data={"email": "test@mail.ru",
                                                                                             "text": "Create message"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.filter(chat=self.chat).count(), 3)
        self.assertEqual(Message.objects.latest('created').author, self.user)
        self.assertEqual(Message.objects.latest('created').ip, None)


class ChatTestCase(APITestCase):

    def setUp(self) -> None:
        self.chat = Chat.objects.create(title="Test",
                                        slug="test",
                                        description="Chat for test",
                                        public=True)

    def test_chat_list(self) -> None:
        response = self.client.get(reverse("chat-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_chat_details(self) -> None:
        response = self.client.get(reverse("chat-details", args=(self.chat.slug,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
