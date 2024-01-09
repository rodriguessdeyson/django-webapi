from rest_framework import serializers
from repository.models import Component
from repository.models import Manufacturer
from .manufacturerSerializer import ManufacturerSerializer

class ComponentSerializer(serializers.ModelSerializer):
    manufacturers = serializers.SerializerMethodField()

    class Meta:
        model = Component
        fields = ("id", "name", "type", "description", "aqtech_part_number", "foot_print", "manufacturers")

    def get_manufacturers(self, obj):
        manufacturerSet = Manufacturer.objects.filter(component_id = obj.id)
        manufacturers = {}
        manufacturerSerialized = ManufacturerSerializer(manufacturerSet, many = True)
        if manufacturerSerialized.is_valid:
            manufacturers = manufacturerSerialized.data
        return manufacturers