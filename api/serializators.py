from Beauty.models import Master
from rest_framework import serializers

class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'