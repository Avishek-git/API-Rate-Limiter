from django.urls import include, path
from onboard import views

urlpatterns = [
    path('api-gateway',views.onboard,name='onboard'),
]