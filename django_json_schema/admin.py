import json

from django.contrib import admin
from django import forms

from .models import JsonSchema

class IndentedJSONEncoder(json.JSONEncoder):
    def __init__(self, *args, indent, sort_keys, **kwargs):
        super().__init__(*args, indent=2, **kwargs)


class JsonSchemaAdminForm(forms.ModelForm):
    schema = forms.JSONField(encoder=IndentedJSONEncoder)

    class Meta:
        model = JsonSchema
        fields = '__all__'


@admin.register(JsonSchema)
class JsonSchemaAdmin(admin.ModelAdmin):
    form = JsonSchemaAdminForm
    search_fields = ["name"]
