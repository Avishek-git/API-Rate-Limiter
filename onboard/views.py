import random
import string
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Service
from onboard.serializers import ServiceSerializer
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
def onboard(request):
    serializer = ServiceSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        endpoint = serializer.validated_data['endpoint']
        rate_limit = serializer.validated_data['rate_limit']
        custom_endpoint = "www.apigateway.com/"
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(6))
        custom_endpoint = custom_endpoint+short_url
        data = Service(name=name,endpoint=endpoint,rate_limit=rate_limit,custom_endpoint=custom_endpoint)
        data.save()
        return Response({"Error":None,"Code":custom_endpoint})
    return Response({"Error":"Unavle to onboard service","Code":None})