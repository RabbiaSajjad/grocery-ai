from django.db import models
from django.contrib.auth.models import User

class GroceryPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="grocery_plans")
    prompt = models.TextField()
    meal_plan = models.JSONField()
    grocery_list = models.JSONField()
    estimated_cost = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Grocery Plan {self.id}"