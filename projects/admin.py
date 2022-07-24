from django.contrib import admin

from .models import Project, ProjectUpdate, ProjectComment

class CommentsInLine(admin.TabularInline):
    model = ProjectComment

class UpdatesInLine(admin.TabularInline):
    model = ProjectUpdate

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        UpdatesInLine,
        CommentsInLine,
    ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectUpdate)
admin.site.register(ProjectComment)

# Register your models here.
