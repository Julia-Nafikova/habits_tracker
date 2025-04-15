from rest_framework import serializers

from users.models import User
from users.validators import validate_telegram_nick


class UserSerializer(serializers.ModelSerializer):
    tg_nick = serializers.CharField(validators=[validate_telegram_nick])

    class Meta:
        model = User
        fields = "__all__"
