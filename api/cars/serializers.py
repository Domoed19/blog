from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=200)
    color = serializers.CharField(max_length=200)
    text = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
