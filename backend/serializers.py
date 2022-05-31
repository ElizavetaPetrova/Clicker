from rest_framework.serializers import ModelSerializer
from .models import Core, Boost
from rest_framework import serializers


class CoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Core
        fields = ['coins', 'click_power'] # Не возвращаем пользователя потому что а зачем


class BoostSerializer(ModelSerializer):
    class Meta:
        model = Boost
        fields = '__all__'