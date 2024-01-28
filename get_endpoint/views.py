from django.core.cache import cache
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from onboard.models import Service
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def get_endpoint(request):
    custom_endpoint = request.GET.get('custom_endpoint')
    try:
        data = Service.objects.get(custom_endpoint=custom_endpoint)
        endpoint = data.endpoint
        rate_limit = data.rate_limit
        time_frame = 60
        hit_count = cache.get(custom_endpoint,0)
        if hit_count>=rate_limit:
            return Response({"Error":"Rate Limit Exceeded"})
        cache.set(custom_endpoint,hit_count+1,time_frame)
        return redirect(endpoint)
    except Service.DoesNotExist:
        return Response({"Error":"Invalid Custom Endpoint"})
    except Exception as e:
        return Response({"Error":str(e)})