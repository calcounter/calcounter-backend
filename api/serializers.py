from rest_framework import serializers
from api.models import Meal


class MealSerializer(serializers.Serializer):
    class Meta:
        model = Meal
        fields = ('mealId', 'description', 'calories', 'datetime')
