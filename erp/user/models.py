# models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None  # Remove the username field
    email = models.EmailField(_('email address'), unique=True)

    # Your custom fields and additional code here

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_("groups"),
        blank=True,
        related_name="custom_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_("user permissions"),
        blank=True,
        related_name="custom_user_set",
        related_query_name="user",
    )

    USERNAME_FIELD = 'email'  # Update this line to use 'email' as the username field
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # Your custom methods and fields here

    def __str__(self):
        return self.email  # Display email instead of username in admin

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    birthdate = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    educational_background = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.email