from django.db import models


class Post(models.Model):
    city = models.CharField(max_length=300, null=False, blank=False)
    body = models.CharField(max_length=160, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body