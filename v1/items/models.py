from django.db import models
from v1.commons.models.created_modified import CreatedModified
from v1.users.models import User


# Create your models here.
class Item(CreatedModified):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
