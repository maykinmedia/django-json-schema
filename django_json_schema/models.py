from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from jsonschema import Draft202012Validator, validate
from jsonschema.exceptions import (
    SchemaError,
    ValidationError as JsonSchemaValidationError,
)


class JsonSchema(models.Model):
    name = models.CharField(
        _("name"), help_text=_("Name of the json schema."), max_length=200
    )

    schema = models.JSONField(
        _("schema"), help_text=_("The schema that can be validated against.")
    )

    class Meta:
        verbose_name = _("Json schema")
        verbose_name_plural = _("Json Schemas")

    def __str__(self):
        return self.name

    def clean(self):
        try:
            Draft202012Validator.check_schema(self.schema)
        except SchemaError as e:
            raise ValidationError(e.message)

    def validate(self, json: dict) -> None:
        try:
            validate(json, self.schema, cls=Draft202012Validator)
        except JsonSchemaValidationError as e:
            raise ValidationError(e.message)
