from rest_framework import serializers

from shop.models import COLOR_CHOICES



class PurchaseUserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=200)


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    color = serializers.ChoiceField(choices=COLOR_CHOICES)
    cost = serializers.IntegerField()

class PurchaseSerializer(serializers.Serializer):
    user = serializers.CharField()
    product = ProductSerializer()
    total = serializers.SerializerMethodField()


    def get_total(self, obj):
        return obj.product.cost * obj.count

