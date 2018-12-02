from django.db import models


class Score(models.Model):

    username = models.CharField(max_length=100, unique=True)
    score_ms = models.FloatField('Score en milisegundos')
    created = models.DateTimeField(auto_now_add=True)
