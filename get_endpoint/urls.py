from django.urls import include, path
from get_endpoint import views

urlpatterns = [
    path('',views.get_endpoint,name='get-endpoint'),
]