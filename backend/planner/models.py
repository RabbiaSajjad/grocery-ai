# planner/models.py

from django.db import models
from django.contrib.auth.models import User

class GroceryPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.TextField()
    meal_plan = models.JSONField()
    grocery_list = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)