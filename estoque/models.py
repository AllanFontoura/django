from django.db import models
from datetime import datetime


class Estoque(models.Model):
    sku = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    preco = models.FloatField()
    max_estoque = models.IntegerField()
    min_estoque = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now, blank=True)

