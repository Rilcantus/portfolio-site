from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name: str = "project_list.html"


class ProjectDetailView(DetailView):
    model = Project
    template_name: str = "project_detail.html"


class ProjectUpdateView(UpdateView):
    model = Project
    fields = (
        "title",
        "overview",
    )
    template_name: str = "project_edit.html"


class ProjectDeleteView(DeleteView):
    model = Project
    template_name: str = "project_delete.html"
    success_url = reverse_lazy("project_list")