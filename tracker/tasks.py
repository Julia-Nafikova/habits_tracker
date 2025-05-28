from celery import shared_task
from django.utils import timezone

from tracker.models import UsefulHabit
from tracker.services import send_telegram_message


@shared_task
def send_reminder():
    """Отправляет пользователю в телеграм напоминание о привычке во время её начала."""
    habits = UsefulHabit.objects.all()
    for habit in habits:
        if habit.time <= timezone.now().time():
            chat_id = habit.user.chat_id
            message = f"Пора выполнять: {habit.action}"
            send_telegram_message(chat_id, message)
