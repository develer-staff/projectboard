from django.contrib import admin
from projects.models import Project, Technology, StatusUpdate

class StatusUpdateInline(admin.StackedInline):
	model = StatusUpdate
	extra = 0

class ProjectAdmin(admin.ModelAdmin):
	filter_horizontal = ('technologies',)
	inlines = (
		StatusUpdateInline,
	)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology)