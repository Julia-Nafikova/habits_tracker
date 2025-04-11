from django.core.validators import MaxValueValidator
from rest_framework import serializers

from tracker.models import UsefulHabit, PleasantHabit


class UsefulHabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsefulHabit
        fields = "__all__"


class PleasantHabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = PleasantHabit
        fields = "__all__"
        