from django.db import models

from django.contrib.auth.models import User


# class MyUser(User):
#     icon=models.ImageField(upload_to='icons/%Y/%m/%d/')
#     class Meta:
#         db_table='myuser'
#











class User_table(models.Model):
    username = models.CharField(max_length=36,unique=True,verbose_name='用户名')
    password = models.CharField(max_length=35,verbose_name='密码')
    email = models.CharField(max_length=64,unique=True,verbose_name='邮箱')
    icon = models.ImageField(upload_to='icons/%Y/%m/%d/')

    class Meta:
        db_table = "User_table"
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

