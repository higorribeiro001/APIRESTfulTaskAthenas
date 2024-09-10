from .views import IdealWeightMixin
from django.urls import path

urlpatterns = [
    path("api/v1/<int:id>/", IdealWeightMixin.as_view(), name="ideal-weight-api")
]
