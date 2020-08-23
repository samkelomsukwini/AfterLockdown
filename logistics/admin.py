from django.contrib import admin

from .models import OperatingSystem, PostCount


admin.site.register(OperatingSystem)
admin.site.register(PostCount)