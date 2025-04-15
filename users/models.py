from django.contrib.auth.models import AbstractUser, UserManager

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Manager(UserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Пользователь должен иметь email')
        user=self.model(email=email,)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None):
        user=self.model(email=email,)
        user.username=""
        user.is_staff=True
        user.is_superuser=True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Введите email")
    tg_nick = models.CharField(max_length=33, verbose_name="Telegram-ник",
                               help_text="Введите telegram-ник")
    avatar = models.ImageField(
        upload_to="users/avatars/", blank=True, null=True, verbose_name="Аватар", help_text="Загрузите аватар"
    )
    phone_number = PhoneNumberField(blank=True, null=True, verbose_name="Телефон", help_text="Введите номер телефона")
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город", help_text="Введите город")

    objects = Manager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
