from django.db import models
from v1.commons.models.created_modified import CreatedModified


class Province(CreatedModified):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
