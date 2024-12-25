from rest_framework import serializers
from .models import CMPPAR


class CMPPARSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMPPAR
        fields = '__all__'
