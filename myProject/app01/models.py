from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=20)
    user_pwd=models.CharField(max_length=20)
