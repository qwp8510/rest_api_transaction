from django.db import models


class Receivers(models.Model):
    name = models.CharField(max_length=30)
    targets = models.JSONField()
    receiveFrequency = models.CharField(max_length=10)
    lineToken = models.CharField(max_length=80, blank=True)

    class Meta:
        db_table = 'receivers'
