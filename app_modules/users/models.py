from django.db import models
from django.contrib.auth.models import AbstractUser
from app_modules.base.models import BaseModel


class User(AbstractUser, BaseModel):
    ADMIN = "admin"
    EMPLOYEE = "employee"

    USER_ROLE = (
        (ADMIN, "Admin"),
        (EMPLOYEE, "Employee"),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    email = models.EmailField(('Email'), unique=True)
    full_name = models.CharField(('Full Name'), max_length=50)
    image = models.FileField(upload_to='user-profile', null=True, blank=True)
    role = models.CharField(('Role'), choices=USER_ROLE, max_length=50, default=EMPLOYEE)

    def __str__(self):
        return self.full_name