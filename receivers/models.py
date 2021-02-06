from django.db import models


class Receivers(models.Model):
    name = models.CharField(max_length=30)
    targets = models.JSONField()
    receiveFrequency = models.CharField(max_length=10)

    class Meta:
        db_table = 'receivers'
