from rest_framework import serializers
from api.models import Meal, Profile
from django.contrib.auth.models import User


class MealSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Meal
        fields = ('id', 'description', 'calories', 'owner', 'created')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    meals = serializers.HyperlinkedRelatedField(many=True, view_name='meal-detail', read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'calorie_goal', 'meals')
