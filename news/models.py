from django.db import models

class News(models.Model):
    source = models.CharField(max_length=200000000, null=False, blank=False, default='covid19 latest')
    call_id = models.CharField(max_length=160, null=True, blank=True)
    author = models.CharField(max_length=200000000, null=True, blank=True)
    title = models.CharField(max_length=200000000, null=False, blank=False)
    content = models.CharField(max_length=200000000, null=True, blank=True)
    url = models.CharField(max_length=200000000, null=False, blank=False)
    urlToImage = models.CharField(max_length=200000000, null=True, blank=True)
    publishedAt = models.CharField(max_length=200000000, null=False, blank=False)

    def __str__(self):
        return self.url

