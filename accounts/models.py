from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

# Create your models here.

class CustomUserManager(UserManager):
    """
    Custom user manager that takes in email as the primary indentifier instead of the username
    """
    def create_user(self, email, password = None, **extra_fields):
        if not email:
            raise ValueError("The email field must be set!")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be a staff")
        if extra_fields.get('is_active') is not True:
            raise ValueError("Superuser must be active")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be 'is_superuser'")
        
        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=150, unique=False, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email' # using email as the unique indentifier instead of the default username
    REQUIRED_FIELDS = []


    