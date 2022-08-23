
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from api.purchases.serializers import PurchSerializer
from shop.models import Product, Purchase
from rest_framework.permissions import IsAuthenticated


class PurchaseListViewSet(ListAPIView):
    """
    API endpoint that allows get a list of posts.
    """

    queryset = Purchase.objects.all().order_by("title")
    serializer_class = PurchSerializer
    permission_classes = []


    def get(self, request, *args, **kwargs):
        queryset = Purchase.objects.all()
        serializer_for_queryset = PurchSerializer(many=True)
        return Response(serializer_for_queryset)
