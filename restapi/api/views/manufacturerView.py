from rest_framework import generics
from repository.models.manufacturerModel import Manufacturer
from ..serializers.manufacturerSerializer import ManufacturerSerializer

class ManufacturerList(generics.ListCreateAPIView):
    serializer_class = ManufacturerSerializer

    def get_queryset(self):
        queryset = Manufacturer.objects.all()
        manufacturer = self.request.query_params.get('manufacturer')
        if manufacturer is not None:
            queryset = queryset.filter(name = manufacturer)
        return queryset

class ManufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ManufacturerSerializer

    queryset = Manufacturer.objects.all()