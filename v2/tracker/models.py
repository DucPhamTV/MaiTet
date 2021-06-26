from uuid import uuid4

from django.db import models

# Create your models here.
from v1.commons.models.created_modified import CreatedModified
from v1.users.models import User


class Tracker(CreatedModified):
    Status = [
        ("PENDING", "pending"),
        ("ACTIVE", "active"),
        ("DONE", "done"),
        ("FAILED", "failed"),
        ("CANCEL", "cancel"),
    ]
    description = models.CharField(max_length=50, null=True, default="No description")
    status = models.CharField(max_length=10, choices=Status, null=True, default="PENDING")
    url = models.URLField(max_length=200, null=False)
    target = models.CharField(max_length=200, null=False)
    created_by = models.ForeignKey(
        User, related_name='create_user',
        on_delete=models.CASCADE, blank=False, null=False)
    check_interval = models.IntegerField(null=True)
    webhook = models.URLField(max_length=200, null=True)
    def __str__(self):
        return f"{self.uuid} | {self.description} | {self.url[:20]} | {self.status}"
