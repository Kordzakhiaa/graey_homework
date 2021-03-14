from django.urls import path
from user.views import RegisterAPIView, UserDetailView

app_name = 'user'

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register_view'),
    path('user_detail/', UserDetailView.as_view(), name='detail_view'),
]
