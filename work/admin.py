from django.contrib import admin
from work.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'added_date', 'project_image', 'is_public']


# Register your models here.
admin.site.register(Project, ProjectAdmin)
