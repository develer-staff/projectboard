from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from projects.models import Project, Technology, StatusUpdate, TeamMember

class StatusUpdateInline(admin.StackedInline):
	model = StatusUpdate
	extra = 0

class ProjectAdmin(admin.ModelAdmin):
	filter_horizontal = ('technologies',)
	inlines = (
		StatusUpdateInline,
	)

class TeamMemberInline(admin.StackedInline):
    model = TeamMember
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (TeamMemberInline, )

admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
