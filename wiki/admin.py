from django.contrib import admin

# Register your models here.

from .models import Page, UserFileUpload

admin.site.register(Page) #page registered to admin site.

admin.site.register(UserFileUpload) #File upload registered to admin site