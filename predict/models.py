from django.db import models

class Review(models.Model):
    text = models.TextField()
    pred_sentiment = models.CharField(max_length=10)
    pred_rating = models.SmallIntegerField()
    model = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.text[:20] + '...'