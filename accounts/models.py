# -*- coding: utf-8  -*-
# © Kan IT AB.
# Written by Tobias Alm
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from common import const


class CustomUserManager(BaseUserManager):

    def create_user(self,
                    email: str,
                    password: str = None,
                    is_admin: bool = False,
                    is_staff: bool = False,
                    is_active: bool = True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        user = self.model(
                email=self.normalize_email(email)
                )
        user.set_password(password)  # change password to hash
        user.is_admin = is_admin
        user.is_staff = is_staff
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self,
                         email: str,
                         password: str = None,
                         **kwargs):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        user = self.model(
                email=self.normalize_email(email)
                )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        user.is_active = True
        return user


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=254,
                              unique=True)
    roles = models.IntegerField(db_column='COL_ROLES',
                                default=const.USER_ROLE_NORMAL)
    objects = CustomUserManager()
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    @property
    def is_administrator(self):
        return self.roles & const.USER_ROLE_ADMINISTRATOR == const.USER_ROLE_ADMINISTRATOR

    @property
    def username(self):
        return self.email

    class Meta:
        db_table = 'T_CUSTOM_USER'
