from rest_framework import serializers
from api_app.models import Monitor

class MonitorSerializer(serializers.ModelSerializer):


    class Meta:
        model = Monitor
        fields = '__all__'