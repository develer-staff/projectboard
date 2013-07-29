from django.db import models
from django.contrib.auth.models import User


class Technology(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class TeamMember(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    avatar = models.ImageField(upload_to='avatars')

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    progress = models.PositiveSmallIntegerField(default=0)
    technologies = models.ManyToManyField(Technology)
    team_members = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name

class StatusUpdate(models.Model):
    date = models.DateField()
    text = models.TextField()
    project = models.ForeignKey('Project')

    class Meta:
        ordering = ('-date',)

    def __unicode__(self):
        return "Update of %s" % self.date
