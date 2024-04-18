from django.db import models

# INTERNAL
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

# USER 
class CustomUserModel(AbstractUser):
    # LETS MAKE SOME CUSTOME ROLES 
    # class Roles(models.TextChoices):
    #     ADMIN = "ADMIN", "Admin"
    #     CUSTOMER = "CUSTOMER", "CUSTOMER"

    Roles = (
    ('ADMIN', 'ADMIN'),
    ('CUSTOMER', 'CUSTOMER'))
      
    username        = None 
    email           = models.CharField(max_length=100,unique=True)
    mobile          = models.CharField(max_length=20)
    profile_img     = models.ImageField(null=True,blank=True)
    bio             = models.TextField(null=True,blank=True) 
    type            = models.CharField(choices=Roles,max_length=100)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # DEFINING OUR NEW MANAGER 
    objects = CustomUserManager()

    def __str__(self):
        return str(self.email) +'||'+ str(self.mobile)

# USER ADDRESS 
class UserAddress(models.Model):
    ADDRESS_TYPE_CHOICES = (
        ('HOME', 'Home'),
        ('OFFICE', 'Office'),
        ('OTHER', 'Other')
    )

    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='addresses')
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE_CHOICES, default='HOME')

    def __str__(self):
        return f"{self.address_line}, {self.city}, {self.country}"
