from django.db import models


class OperatingSystem(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.name