from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    result = {
        "date" : "2020-01-01",
        "bulk_id": 1,
        "id": 1,
        "gene_type": "gene",
        "name": "gene1",
        "organ": "lungs",
        "date" : "2020-01-01",
    }
    
    return Response(result)