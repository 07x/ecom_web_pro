from django.contrib import admin
from .models import CustomUserModel , UserAddress

# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(UserAddress)


