from rest_framework import serializers

from .models import GroceryPlan

class GroceryPlanRequestSerializer(serializers.Serializer):
    prompt = serializers.CharField()

class GroceryPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryPlan
        fields = "__all__"