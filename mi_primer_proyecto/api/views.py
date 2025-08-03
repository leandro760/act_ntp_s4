from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

class HelloWorldView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hola Mundo"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def greet_view(request):
    return Response({"message": "Hola Mundo"})

