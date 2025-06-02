from rest_framework import serializers
from .models import Approvalmodel
from django.contrib.auth.models import User
class Approval1(serializers.ModelSerializer):

    class Meta:
        model=Approvalmodel
        fields="__all__"


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()