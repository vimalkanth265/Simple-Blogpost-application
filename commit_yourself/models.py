from typing import Text
from django.db import models
from django.db.models.fields import TextField
from django.forms.fields import CharField, DateTimeField
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.
class BlogPost(models.Model):
    Title=models.CharField(max_length=100)
    Content=models.TextField()
    DatePosted=models.DateTimeField(default=timezone.now)
    Author=models.ForeignKey(User,on_delete=models.CASCADE)


class profile(models.Model):
    user_first=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self) -> str:
        return f'{self.user_first.username} profile ' 