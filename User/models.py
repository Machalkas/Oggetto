from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.models import PermissionsMixin
# from django.core.mail import send_mail

class Manager(UserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Пользователь должен иметь email')
        user=self.model(email=email,)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None):
        user=self.model(email=email)
        # user.username=""
        user.is_staff=True
        user.is_superuser=True
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):
    username = None
    first_name=None
    last_name=None
    email = models.EmailField('Email', unique=True)
    is_shop = models.BooleanField(null=False, default=False, blank=True, verbose_name="Магазин?")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects=Manager()
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    def save(self,*args,**kwargs):
        # try:
        #     if User.objects.get(email=self.email).is_specialist==False and self.is_specialist==True:
        #         send_mail('Хакатон | Изменение прав пользователя', 'Ваши права пользователя были изменены, теперь вы являетесь кейсодателем. Вы можете зарегестрировать свою компанию и публековать кейсы от лица этой компании', '', [self.email], fail_silently=True)
        # except:
        #     pass
        super().save(*args,**kwargs)