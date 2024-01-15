from repository.models.componentModel import Component
from ..serializers.componentSerializer import ComponentSerializer

class ComponentRepository():
    def get_object(self, id):
        try:
            return Component.objects.get(pk = id)
        except Component.DoesNotExist:
            return None

    def select_many(self):
        componentSet = Component.objects.all()
        components = ComponentSerializer(componentSet, many = True)
        return components.data

    def create(self, data):
        component_model = ComponentSerializer(data = data)
        if component_model.is_valid():
            component_model.save()
            return component_model.data

    def select(self, pk):
        try:
            component = self.get_object(id = pk)
            component = ComponentSerializer(component, many = False)
            return component.data
        except component.DoesNotExist:
            return None 

    def delete(self, pk):
        component = self.get_object(id = pk)
        component.delete()

    def update(self, data, pk):
        component = self.get_object(id = pk)
        if component is not None:
            componentModel = ComponentSerializer(component, data = data)
            if componentModel.is_valid():
                componentModel.update()