from django.contrib import admin

# Register your models here.

from .models import Page, UserFileUpload

admin.site.register(Page)

admin.site.register(UserFileUpload)