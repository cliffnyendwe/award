from django.contrib import admin

from django.contrib import admin
from .models import Project,Profile

admin.site.register(Project)
admin.site.register(Profile)
# admin.site.register(Rating)