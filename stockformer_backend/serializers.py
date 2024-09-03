from rest_framework import serializers

class ForecastSerializer(serializers.Serializer):
    symbol = serializers.CharField(max_length=10)
    prediction_length = serializers.IntegerField(min_value=1)
