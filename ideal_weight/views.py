from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models import Person
from tasks.serializers import PersonSerializer

class IdealWeightMixin(APIView):

    def get(self, request, id):
        try:
            serializer = PersonSerializer(Person.objects.get(id=id), many=False)
            return Response(
                {
                    'user': serializer.data['name'],
                    'ideal_weight': (72.7 * serializer.data['height']) - 58 if str(serializer.data['sex']).lower() == 'm' else (62.1 * serializer.data['height']) - 44.7
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                { 'error': str(e) },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
