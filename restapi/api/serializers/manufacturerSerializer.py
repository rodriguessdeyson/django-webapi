from rest_framework import serializers
from repository.models import Manufacturer
# from .componentSerializer import ComponentSerializer

class ManufacturerSerializer(serializers.ModelSerializer):
    # components = serializers.SerializerMethodField()

    class Meta:
        model = Manufacturer
        fields = ("id", "name", "part_number", "datasheet")

    def get_components(self, obj):
        componentSet = obj.component
        data = {}
        components = ComponentSerializer(componentSet)
        if components.is_valid:
            data = components.data
        return data