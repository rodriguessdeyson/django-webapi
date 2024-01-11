from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from repository.data.componentRepository import ComponentRepository

class ComponentViewList(APIView):
    def get(self, request):
        repository = ComponentRepository()
        components = repository.select_many()
        return Response(components, status = status.HTTP_200_OK)

    def post(self, request):
        repository = ComponentRepository()
        requestData = request.data
        component = repository.create(data = requestData)
        return Response(component, status = status.HTTP_201_CREATED)

class ComponentViewDetail(APIView):
    def get(self, request, id):
        repository = ComponentRepository()
        component = repository.select(pk = id)
        if component is None:
            return Response(status = status.HTTP_404_NOT_FOUND)
        return Response(component, status = status.HTTP_200_OK)

    def put(self, request, id):
        repository = ComponentRepository()
        requestData = request.data
        component = repository.update(data = requestData, pk = id)
        return Response(component, status = status.HTTP_200_OK)

    def delete(self, request, id):
        repository = ComponentRepository()
        repository.delete(pk = id)
        return Response(status = status.HTTP_202_ACCEPTED)
