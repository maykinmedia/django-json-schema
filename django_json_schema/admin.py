from django.contrib import admin

from .models import JsonSchema


@admin.register(JsonSchema)
class JsonSchemaAdmin(admin.ModelAdmin):
    search_fields = ["name"]
