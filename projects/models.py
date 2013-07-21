from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    progress = models.PositiveSmallIntegerField()
    technologies = models.ManyToManyField(Technology)

    def __unicode__(self):
        return self.name
