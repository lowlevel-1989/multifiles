from __future__ import unicode_literals

from django.db import models

class File(models.Model):
    name = models.CharField(max_length=80)
    file = models.FileField(upload_to='ticket/%Y/%m/%d')

    def __str__(self):
        return self.name

class Ticket(models.Model):
    files = models.ManyToManyField(File)
