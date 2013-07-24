from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    progress = models.PositiveSmallIntegerField(default=0)
    technologies = models.ManyToManyField(Technology)

    def __unicode__(self):
        return self.name
