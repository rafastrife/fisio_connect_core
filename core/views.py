from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import HealthCheckSerializer


# Create your views here.


@api_view(['GET'])
def health_check(request):
    """
    Endpoint para verificação de saúde da API
    """
    serializer = HealthCheckSerializer()
    return Response(serializer.data, status=status.HTTP_200_OK)
