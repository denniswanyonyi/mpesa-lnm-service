
from django.urls import path
from .views import index, c2b_validation, c2b_confirmation, c2b_status_query

urlpatterns = [
    path('', index),
    path('c2b/validation', c2b_validation),
    path('c2b/confirmation', c2b_confirmation), 
    path('c2b/status-query', c2b_status_query)
]