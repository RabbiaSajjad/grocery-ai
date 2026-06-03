from rest_framework import serializers

class GroceryPlanRequestSerializer(serializers.Serializer):
    prompt = serializers.CharField()