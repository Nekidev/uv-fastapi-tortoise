from tortoise import fields
from tortoise.models import Model

from project.db.fields import NanoIDField


class Book(Model):
    id = NanoIDField(primary_key=True)

    title = fields.CharField(max_length=255)
    author = fields.CharField(max_length=255)

    published_at = fields.DatetimeField(null=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
