from django.db import models


class Meal(models.Model):
    mealId = models.IntegerField(unique=True)
    description = models.CharField(max_length=200)
    calories = models.CharField(max_length=5)
    datetime = models.DateTimeField()

    def __str__(self):
        return self.description



