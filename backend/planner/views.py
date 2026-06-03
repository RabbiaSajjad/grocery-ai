from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from pantry.models import PantryItem

from .services import generate_grocery_plan
from .serializers import GroceryPlanRequestSerializer, GroceryPlanSerializer
from .models import GroceryPlan

class GeneratePlanView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = GroceryPlanRequestSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        pantry_items = list(  
            PantryItem.objects.filter(
                user=request.user
            ).values_list("name", flat=True)
        )

        result = generate_grocery_plan(
            serializer.validated_data["prompt"],
            pantry_items,
        )

        GroceryPlan.objects.create(
            user=request.user,
            prompt=serializer.validated_data["prompt"],
            meal_plan=result["meal_plan"],
            grocery_list=result["grocery_list"],
            estimated_cost=result["estimated_total_cost"]
        )

        return Response(result)

class GroceryPlanHistoryView(generics.ListAPIView):
    serializer_class = GroceryPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return GroceryPlan.objects.filter(
            user=self.request.user
        ).order_by("-created_at")