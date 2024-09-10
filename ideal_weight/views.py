from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models import Person
from tasks.serializers import PersonSerializer

class IdealWeightMixin(APIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, id):
        return Response(
            {
                'user': self.PersonSerializer(self.Person.filter(id=id), many=False).data,
                'ideal_weight': (72.7 * request.data['height']) - 58 if str(request.data['sex']).lower() == 'm' else (62.1 * request.data['height']) - 44.7
            },
            status=status.HTTP_200_OK
        )

