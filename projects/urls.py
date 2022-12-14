from django.urls import path

from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectUpdateView,
    ProjectDeleteView,
    ProjectCreateView,

)

urlpatterns = [
    path("<int:pk>/", ProjectDetailView.as_view(),
        name="project_detail"),
    path("<int:pk>/edit/", ProjectUpdateView.as_view(),
        name="project_edit"),
    path("<int:pk>/delete/", ProjectDeleteView.as_view(),
        name="project_delete"),
    path("new/", ProjectCreateView.as_view(), name="project_new"),
    path("", ProjectListView.as_view(), name="project_list"),
]
