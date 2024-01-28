from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('summary/<int:pk>/',scrap_summary,name='summary'),
    path('api/',scrap_api,name='api'),
]