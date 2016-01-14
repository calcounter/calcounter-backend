from rest_framework import serializers
from api.models import Meal, Profile
from django.contrib.auth.models import User


class MealSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Meal
        fields = ('id', 'description', 'calories', 'owner', 'created', 'datetime')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'calorie_goal')
