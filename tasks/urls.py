from rest_framework.routers import SimpleRouter
from .views.task import TaskViewSet

app_name = 'person'
person_api_v1_router = SimpleRouter()

person_api_v1_router.register(
    'api/v1',
    TaskViewSet,
    basename='person-api'
)

urlpatterns = person_api_v1_router.urls