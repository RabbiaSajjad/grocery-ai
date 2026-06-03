from rest_framework import serializers

from .models import GroceryPlan

class GroceryPlanRequestSerializer(serializers.Serializer):
    prompt = serializers.CharField()

class GroceryPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryPlan
        fields = "__all__"
        read_only_fields = ["user", "created_at"]