from django import template
register = template.Library()

from ..models import Project, Technology, StatusUpdate

@register.inclusion_tag('projects/show_project_list.html', takes_context=True)
def show_project_list(context):
    project_list = [
        {
                'id': project.pk,
                'name': project.name,
                'progress': project.progress,
                'technologies': project.technologies.all(),
        }
        for project in Project.objects.all().order_by('start_date')
    ]
    context.update({'project_list': project_list})
    return context

@register.inclusion_tag('projects/show_project_detail.html', takes_context=True)
def show_project_detail(context, project_id):
    project_detail = Project.objects.get(pk=project_id)

    context.update({'project_detail': project_detail})
    return context

@register.inclusion_tag('projects/show_project_technologies.html', takes_context=True)
def show_project_technologies(context, project_id):
    technologies = Technology.objects.filter(project=project_id)

    context.update({'project_technologies': technologies})
    return context

@register.inclusion_tag('projects/show_project_updates.html', takes_context=True)
def show_project_updates(context, project_id):
    updates = StatusUpdate.objects.filter(project=project_id)

    context.update({'project_updates': updates})
    return context