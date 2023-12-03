from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.api_one, name='api_one')
]