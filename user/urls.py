from django.urls import path
from user.views import RegisterAPIView

app_name = 'user'

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register_view'),
    
]
