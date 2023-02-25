from django.contrib import admin

# Register your models here.
from .models import Project, Project_buffer

admin.site.register(Project)
admin.site.register(Project_buffer)