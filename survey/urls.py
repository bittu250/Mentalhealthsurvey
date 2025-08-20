from django.urls import path
from .views import survey_view, success_view

urlpatterns = [
    path("", survey_view, name="survey"),
    path("success/", success_view, name="success")

   
]