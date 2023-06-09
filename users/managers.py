from django.contrib.auth.models import (
    BaseUserManager,
)


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, name, number, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError("Вы не ввели email!")
        if not name:
            raise ValueError("Вы не ввели ФИО!")
        if not number:
            raise ValueError("Вы не ввели ваш номер!")
        if not password:
            raise ValueError("Вы не ввели пароль!")
        user = self.model(
            email=email,
            name=name,
            number=number,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def _create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Вы не ввели ваше email !")
        if not password:
            raise ValueError("Вы не ввели пароль!")
        superuser = self.model(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )
        if password:
            superuser.set_password(password)
        superuser.save(using=self._db)
        return superuser

    def create_user(
            self,
            email,
            name,
            number,
            password=None,
            **extra_fields
    ):

        return self._create_user(email, name, number, password, is_staff=False, is_superuser=False,
                                 **extra_fields)

    def create_superuser(
            self,
            email,
            password=None,
    ):

        superuser = self._create_superuser(email, password)
        superuser.save(using=self._db)
        return superuser