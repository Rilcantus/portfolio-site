from pickle import FALSE
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView
)
from django.views import View
from django.urls import reverse_lazy, reverse

from .forms import ProjectCommentForm

from .models import Project

class CommentGet(DetailView):
    model = Project
    template_name: str = "project/project_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProjectCommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Project
    form_class = ProjectCommentForm
    template_name: str = "project/project_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.project = self.object
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        project = self.get_object()
        return reverse("project_detail", kwargs={"pk": project.pkcv})



class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name: str = "project/project_list.html"


class ProjectDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class ProjectUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = (
        "title",
        "overview",
    )
    template_name: str = "project/project_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ProjectDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name: str = "project/project_delete.html"
    success_url = reverse_lazy("project_list")

    def test_func(self):
        obj = self.object()
        return obj.author == self.request.user

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name: str = "project/project_new.html"
    fields = ("title", "overview")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)