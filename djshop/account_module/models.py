from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
#AbstractBaseUser is very simple
#abstractUser is more usable and complete to inherit.
#create models here


class user(AbstractUser):
    mobile = models.CharField(max_length=30,verbose_name="phone_number")
    email_active_code = models.CharField(max_length=100,verbose_name="email_activation_code")

    class Meta:
        verbose_name = "client"
        verbose_name_plural = "clients"

    def __str__(self):
        return self.get_full_name()

