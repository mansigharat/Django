
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.manager import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None

    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    user_id = models.CharField(max_length=50, unique=True)

    user_profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = UserManager()
