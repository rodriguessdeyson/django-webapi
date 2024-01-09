from rest_framework.decorators import api_view
from rest_framework.response import Response
 
@api_view(['GET'])
def APIOverview(request):
    api_urls = {
        'all_components': '/components',
        'Search by id': '/components/id',
        'Search by type': '/components?type=type_name',
        'Add': '/components',
        'Update': '/components/id',
        'Delete': '/components/id'
    }
    return Response(api_urls)