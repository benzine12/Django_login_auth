from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

#free access
@api_view(['GET'])
def public_test(req):
    return HttpResponse("public mode")


#protected zone
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def private_test(req):
    return HttpResponse("private mode ")