from django.db import models

# Create your models here.
from v1.commons.models.created_modified import CreatedModified
from v1.users.models import User


class Tracker(CreatedModified):
    tracker_id = 
    Status = [
        ("PENDING", "pending"),
        ("ACTIVE", "active"),
        ("DONE", "done"),
        ("FAILED", "failed"),
        ("CANCEL", "cancel"),
    ]
    status = models.CharField(max_length=10, choices=Status, null=True, default="PENDING")
    url = models.URLField(max_length=200, null=False)
    target = models.CharField(max_length=200, null=False)
    create_by = models.ForeignKey(
        User, related_name='created_by',
        on_delete=models.CASCADE, blank=False, null=False)
    #result = 
