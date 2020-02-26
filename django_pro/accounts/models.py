from django.db import models

# Create your models here.
class Captcha(models.Model):
    captcha = models.CharField(max_length=10)
