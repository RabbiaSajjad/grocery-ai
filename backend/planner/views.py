from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from pantry.models import PantryItem

from .services import generate_grocery_plan
from .serializers import GroceryPlanRequestSerializer

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

        return Response(result)