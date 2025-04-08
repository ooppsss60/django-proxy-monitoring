from django.db import models

class Flower(models.Model):
    class Meta:
        managed = False
        verbose_name_plural = "Flower"

class Grafana(models.Model):
    class Meta:
        managed = False
        verbose_name_plural = "Grafana"