from rest_framework import serializers


class HealthCheckSerializer(serializers.Serializer):
    """
    Serializer para verificação de saúde da API
    """
    status = serializers.CharField(default="ok")
    message = serializers.CharField(default="API is running") 