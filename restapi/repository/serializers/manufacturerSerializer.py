from rest_framework import serializers
from repository.models import Manufacturer
# from .componentSerializer import ComponentSerializer

class ManufacturerSerializer(serializers.ModelSerializer):
    component_id = serializers.IntegerField(write_only = True)

    class Meta:
        model = Manufacturer
        fields = ("id", "component_id", "name", "part_number", "datasheet")