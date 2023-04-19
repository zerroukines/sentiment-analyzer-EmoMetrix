from django.db import models

class MyUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=100)

class Analyze(models.Model):
    inputField = models.TextField()
    sentimentField = models.CharField(max_length=50 , null=True)

