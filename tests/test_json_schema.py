from django.core.exceptions import ValidationError
from django.test import TestCase

from django_json_schema.models import JsonSchema


class TestJsonSchema(TestCase):
    def setUp(self):
        self.schema = JsonSchema.objects.create(
            name="schema",
            schema={
                "type": "object",
                "properties": {
                    "price": {"type": "number"},
                    "name": {"type": "string"},
                },
                "required": ["price", "name"],
            },
        )

    def test_valid_json(self):
        self.schema.validate(
            {
                "price": 10,
                "name": "test",
            }
        )

    def test_invalid_json(self):
        with self.assertRaisesMessage(
            ValidationError, "'price' is a required property"
        ):
            self.schema.validate({"name": "Eggs"})
