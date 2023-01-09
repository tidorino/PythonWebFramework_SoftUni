from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)
        user.save()

        return user

    # this removes password from the response
    def to_representation(self, instance):
        user_representation = super().to_representation(instance)
        user_representation.pop('password')
        return user_representation

