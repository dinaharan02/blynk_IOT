from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('api/realtime/', views.get_realtime_data),
]