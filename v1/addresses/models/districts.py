from django.db import models
from v1.commons.models.created_modified import CreatedModified
from .provinces import Province


class District(CreatedModified):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    province = models.ForeignKey(
        Province, related_name='%(class)s_province',
        on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
