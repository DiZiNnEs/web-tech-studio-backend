from django.contrib import admin

from main_app.models import Project, Customer


@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    pass


@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    pass
