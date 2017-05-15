from django.db import models
import datetime

date = datetime.date.today


class Gasoline(models.Model):
    rank = models.CharField(max_length=32)
    pref = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    date = models.DateField(default=date)


class HighOctane(models.Model):
    rank = models.CharField(max_length=32)
    pref = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    date = models.DateField(default=date)


class Diesel(models.Model):
    rank = models.CharField(max_length=32)
    pref = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    date = models.DateField(default=date)
