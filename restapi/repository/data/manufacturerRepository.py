from repository.models.manufacturerModel import Manufacturer
from ..serializers.manufacturerSerializer import ManufacturerSerializer

class ManufacturerRepository():
    def get_object(self, id):
        try:
            return Manufacturer.objects.get(pk = id)
        except Manufacturer.DoesNotExist:
            return None

    def select_many(self):
        manufacturerSet = Manufacturer.objects.all()
        manufacturers = ManufacturerSerializer(manufacturerSet, many = True)
        return manufacturers.data

    def create(self, data):
        print(data)
        manufacturerModel = ManufacturerSerializer(data = data)
        if manufacturerModel.is_valid():
            manufacturerModel.save()
            return manufacturerModel.data
        else:
            return None

    def select(self, pk):
        try:
            manufacturer = self.get_object(id = pk)
            manufacturer = ManufacturerSerializer(manufacturer, many = False)
            return manufacturer.data
        except Manufacturer.DoesNotExist:
            return None 

    def delete(self, pk):
        manufacturer = self.get_object(id = pk)
        manufacturer.delete()

    def update(self, data, pk):
        manufacturer = self.get_object(id = pk)
        if manufacturer is not None:
            manufacturerModel = ManufacturerSerializer(manufacturer, data = data)
            if manufacturerModel.is_valid():
                manufacturerModel.update()