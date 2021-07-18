from uuid import uuid4

from django.db import models

# Create your models here.
from v1.commons.models.created_modified import CreatedModified
from v1.users.models import User
from v2.tracker.models import Tracker


class Result(CreatedModified):
    tracker = models.ForeignKey(Tracker, related_name='result', on_delete=models.CASCADE)
    value = models.TextField(max_length=2000)

    def __str__(self):
        return f"{self.tracker.description}, result text length {len(self.value)}"
