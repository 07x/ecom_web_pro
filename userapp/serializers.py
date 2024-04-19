from .models import CustomUserModel 

# INTERNAL 
from django.contrib.auth import get_user_model # type: ignore

# EXTERNAL 
User = get_user_model()





