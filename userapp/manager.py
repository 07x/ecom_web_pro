from django.contrib.auth.base_user import BaseUserManager 


class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('please provide a valid email')
       
        # EMAIL 
        from .models import CustomUserModel
        name =   [c[0] for c in CustomUserModel.Roles.field.choices]
        extra_fields.setdefault('type',name[1])
        email = self.normalize_email(email)
        user  = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user 
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_superuser",True)

        # SUPER USER 
        from .models import CustomUserModel

        name =   [c[0] for c in CustomUserModel.Roles.field.choices]
        extra_fields.setdefault('type',name[0])

        # EXTRA VALIDATION 
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Susperuser must have is_superuser")
        
        return self.create_user(email,password,**extra_fields)


