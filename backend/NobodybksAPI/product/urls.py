from django.urls import path
from .views import  DetailApiView

urlpatterns = [
# path('', api_view, name='api_view'),
    path('detail/<int:pk>/', DetailApiView.as_view()),
]
