from django.contrib import admin
from projects.models import Project, Technology

class ProjectAdmin(admin.ModelAdmin):
	filter_horizontal = ('technologies',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology)