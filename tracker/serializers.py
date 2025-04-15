from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers

from tracker.models import UsefulHabit, PleasantHabit


class UsefulHabitSerializer(serializers.ModelSerializer):
    periodicity = serializers.IntegerField(default=1, validators=[
        MaxValueValidator(7, message="Нельзя выполнять привычку реже, чем 1 раз в 7 дней"),
        MinValueValidator(1, message="Минимальное значение 1")])

    def validate(self, data):
        """Проверяет, что выбрано только одно поле варианта поощрения."""
        if data.get('related_habit') and data.get('award'):
            raise serializers.ValidationError("Выберите только один вариант поощрения")
        return data

    class Meta:
        model = UsefulHabit
        fields = "__all__"


class PleasantHabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = PleasantHabit
        fields = "__all__"
        