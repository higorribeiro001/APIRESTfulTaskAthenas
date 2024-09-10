from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from tasks.models import Person
from tasks.serializers import PersonSerializer

class TaskViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = PageNumberPagination