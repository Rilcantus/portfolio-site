from django.views.generic import ListView

from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name: str = "project_list.html"

