from django.contrib import admin

from .models import Post


admin.site.site_header = 'AfterLockdown'

admin.site.register(Post)