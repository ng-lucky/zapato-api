from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class ZUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have a email')

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(email, 
                                password=password,
                                first_name=first_name,
                                last_name=last_name)
        user.is_admin = True
        user.save(using=self._db)
        return user
    


class ZUser(AbstractBaseUser):
    USER_TYPES = (
        ("ADMIN", "Super Admin"),
        ("CUSTOMER", "Customer"),
        ("MERCHANT", "Merchant")
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=300, unique=True, verbose_name="Email address")
    username = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name="username")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default="CUSTOMER")
    # image = models.ImageField(upload_to="profile_pictures", default='', blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = ZUserManager()

    @property
    def is_staff(self):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    

