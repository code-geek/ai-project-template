"""User models."""

from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model extending Django's AbstractUser."""

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: ClassVar[list[str]] = ["username", "first_name", "last_name"]

    class Meta:
        db_table = "users_user"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.email
