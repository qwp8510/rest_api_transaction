from django.db import models


class Targets(models.Model):
    name = models.CharField(max_length=120, blank=False)
    currency = models.CharField(max_length=20, blank=False)
    fundType = models.CharField(max_length=20, blank=False)
    company = models.CharField(max_length=30, blank=False)
    partition = models.CharField(max_length=20, blank=False)
    dividendFrequency = models.CharField(max_length=10, blank=False)
    url = models.CharField(max_length=150, blank=False)
    code = models.CharField(max_length=20)
