from django.conf import settings
from django.db import models
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})

class ProjectUpdate(models.Model):
    title = models.CharField(max_length=255)
    project = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
    )
    udpate = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("project_list")
    