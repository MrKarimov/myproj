from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


from .managers import CustomUserManager

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_("email address"),unique = True)

    first_name  = models.CharField(_("first name "),max_length=150)
    last_name  = models.CharField(_("last name "),max_length=150)

    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default=True)
    
    data_joined =models.DateTimeField(default = now )
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"