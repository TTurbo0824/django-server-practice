from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    nickname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
