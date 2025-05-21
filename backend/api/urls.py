from django.urls import path
from . import views

urlpatterns = [
    path("projects/", views.ProjectListCreate.as_view(), name="project-list-create"),
    path("projects/delete/<int:pk>/", views.ProjectDelete.as_view(), name="project-delete"),
]