from django.urls import path
from .views import *

urlpatterns = [
    path('details/<int:content_id>/', details, name="details")
]