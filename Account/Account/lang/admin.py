from django.contrib import admin

from .models import *


class LangAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Langv, LangAdmin)
