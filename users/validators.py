from rest_framework import serializers


def validate_telegram_nick(value):
    if not value.startswith("@"):
        raise serializers.ValidationError("Укажите Telegram-ник, начиная с символа '@'")

    if len(value) < 6:
        raise serializers.ValidationError("Длина ника должна быть не менее 6 символов")
