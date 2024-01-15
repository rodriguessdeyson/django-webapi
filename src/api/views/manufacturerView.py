from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from repository.data.manufacturerRepository import ManufacturerRepository

class ManufacturerViewList(APIView):
    def get(self, request):
        repository = ManufacturerRepository()
        manufacturers = repository.select_many()
        return Response(manufacturers, status = status.HTTP_200_OK)

    def post(self, request):
        repository = ManufacturerRepository()
        requestData = request.data
        manufacturer = repository.create(data = requestData)
        if manufacturer is not None:
            return Response(manufacturer, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

class ManufacturerViewDetail(APIView):
    def get(self, request, id):
        repository = ManufacturerRepository()
        manufacturer = repository.select(pk = id)
        print(manufacturer)
        if manufacturer is None:
            return Response(status = status.HTTP_404_NOT_FOUND)
        return Response(manufacturer, status = status.HTTP_200_OK)

    def put(self, request, id):
        repository = ManufacturerRepository()
        requestData = request.data
        manufacturer = repository.update(data = requestData, pk = id)
        return Response(manufacturer, status = status.HTTP_200_OK)

    def delete(self, request, id):
        repository = ManufacturerRepository()
        repository.delete(pk = id)
        return Response(status = status.HTTP_202_ACCEPTED)
