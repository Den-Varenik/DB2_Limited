from re import match

from rest_framework import serializers

from chat.models import Message, Chat


class ChatSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Chat
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    ip = serializers.IPAddressField(read_only=True)
    chat = ChatSerializer(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Message
        fields = "__all__"

    @staticmethod
    def validate_email(value):
        if not match(r"^(\w\.?)+@(\w\.?)+(?<!\.)$", value):
            raise serializers.ValidationError("Enter a valid email address.")
        return value

    @staticmethod
    def validate_text(value):
        if not match(r"^(?!\s*$).{,99}", value):
            raise serializers.ValidationError("Enter a valid text message.")
        return value
