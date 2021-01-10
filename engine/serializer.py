from rest_framework import serializers
from .models import Engine_1

class Engine_1Serializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'engine_name', 'game_name', 'price', 'description')
        model = Engine_1