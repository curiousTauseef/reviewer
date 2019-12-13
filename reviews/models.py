from django.db import models
from django.db.models import Avg, Count


class Content(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    reviews_total = models.FloatField(null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    content = models.ForeignKey(Content, null=True, on_delete=models.CASCADE)
    readability = models.CharField(max_length=500)
    avg_rating = models.IntegerField(null=True)