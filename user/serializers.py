from rest_framework import serializers

from user.models import User
from django.utils.translation import gettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'gender',
            'phone_number',
        ]


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, label=_('Password'))
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, label=_('Repeat password'))

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'gender',
            'phone_number',
            'password',
            'password2',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    # @Todo hint: https://nemecek.be/blog/23/how-to-createregister-user-account-with-django-rest-framework-api
    # def create(self, validated_data):
    #     password = validated_data.pop('password')
    #     user = User(**validated_data)
    #     user.set_password(password)
    #     user.save()
    #     return user

    def save(self):
        user = User(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            phone_number=self.validated_data['phone_number'],
            email=self.validated_data['email'],
            gender=self.validated_data['gender'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            return serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, label=_('Password'))

    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]
