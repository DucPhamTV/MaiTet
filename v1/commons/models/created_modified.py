import uuid
from django.db import models


class CreatedModified(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True, db_index=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True
