from django.contrib import admin

from main_app.models import Project


@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    pass
