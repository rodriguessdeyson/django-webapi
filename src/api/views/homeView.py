from rest_framework.decorators import api_view
from rest_framework.response import Response
 
@api_view(['GET'])
def APIOverview(request):
    api_urls = {
        'All Components': '/components',
        'Search by id': '/components/id',
        'Search by type': '/components?type=type_name',
        'Add': '/components',
        'Update': '/components/id',
        'Delete': '/components/id',
        'Token': '/api/token',
        'Refresh token': '/api/token/refresh',
    }
    return Response(api_urls)