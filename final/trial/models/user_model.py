from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Profile(models.Model):
    role_choices = (
        ('member', 'member'),
        ('Development-Officer', 'Development-Officer'),
        ('Administrative-Secretary', 'Administrative-Secretary'),
    )
    sex_choices = (
        ('male', 'male'),
        ('female', 'female')
    )
    sex = models.CharField(choices=sex_choices, max_length=6)  # Change max_length to an integer
    phone = models.CharField(max_length=15)
    role = models.CharField(choices=role_choices, default='member', max_length=25)  # Change max_length to an integer
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)
