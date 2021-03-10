from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import RegistrationSerializer


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

