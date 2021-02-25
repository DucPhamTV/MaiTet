from django.db import models
from v1.commons.models.created_modified import CreatedModified
from v1.users.models import User
from v1.items.models import Item


# Create your models here.
class Comment(CreatedModified):
    written_by = models.ForeignKey(
        User, related_name='written_by',
        on_delete=models.CASCADE, blank=True, null=True)
    for_item = models.ForeignKey(
        Item, related_name='for_item',
        on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField()
