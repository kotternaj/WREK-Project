from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    url = models.CharField(max_length=100, verbose_name="URL")
    week = models.IntegerField(default=0)
