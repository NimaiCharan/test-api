from rest_framework import serializers
from .models import Test

class TestSerializer(serializers.Serializer):
    #id = serializers.IntegerField()
    name = serializers.CharField()
    test = serializers.CharField()
    roll = serializers.IntegerField()
    
    class Meta:
        model = 'Test',
        fields = ['name', 'test', 'roll']