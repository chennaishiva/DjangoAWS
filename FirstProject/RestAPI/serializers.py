from rest_framework import serializers

from RestAPI.models import userRegister


class userRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = userRegister
        fields = "__all__"
