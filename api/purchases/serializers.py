from rest_framework import serializers




class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    color = serializers.CharField(max_length=200)
    cost = serializers.IntegerField()
    image = serializers.ImageField(read_only=True)

class PurchSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField()
    product = serializers.PrimaryKeyRelatedField()
    count = serializers.IntegerField()

