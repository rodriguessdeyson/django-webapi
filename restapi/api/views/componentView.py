from rest_framework import generics
from repository.models.componentModel import Component
from ..serializers.componentSerializer import ComponentSerializer

class ComponentList(generics.ListCreateAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        queryset = Component.objects.all()
        manufacturer = self.request.query_params.get('manufacturer')
        if manufacturer is not None:
            queryset = queryset.filter(manufacturer = manufacturer)
        return queryset

class ComponentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ComponentSerializer

    queryset = Component.objects.all()