from rest_framework import serializers
from base.models import Shedule


class SheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shedule
        fields = '__all__'